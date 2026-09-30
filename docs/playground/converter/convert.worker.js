// Copyright 2026 TAISEI CORPORATION
// SPDX-License-Identifier: MPL-2.0
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

// ifcopenshellのwasmがcp313-cp313-pyodide_2025_0_wasm32であるため、v29を使用
importScripts("https://cdn.jsdelivr.net/pyodide/v0.29.5/full/pyodide.js");

const IFCOPENSHELL_WHEEL_NAME = "ifcopenshell-0.8.5-cp313-cp313-pyodide_2025_0_wasm32.whl";
const IFCOPENSHELL_WHEEL_URL = "https://ifcopenshell.github.io/wasm-wheels/" + IFCOPENSHELL_WHEEL_NAME;
const IFCOPENSHELL_WHEEL_SHA256 = "fbebb7a7144277be213d156ed9b77de30de1d92b0b2b0c815e4a07555bfb929c";
const STBKIT_PACKAGE_NAME = "stbkit";
const IFCOPENSHELL_PATH = "/tmp/" + IFCOPENSHELL_WHEEL_NAME;
const INPUT_PATH = "/tmp/input.stb";
const LOG_BATCH_INTERVAL_MS = 500;

const CONVERT_SRC = `import stbkit.api

def stbkit_convert_to_ifc(source):
    stb = stbkit.api.load_latest(source)
    ifc = stbkit.api.to_ifc(stb)
    output = ifc.to_string()
    return output
`;

let pyodide = null;
let loadedPython = false;
let pendingLogLines = [];
let logBatchTimerId = null;

function logEmit(line) {
    // 今回の変換ではsqlサポートは不要なので無視する
    if (line.includes("No SQL support")) {
        return;
    }
    pendingLogLines.push(String(line));
    if (logBatchTimerId === null) {
        logBatchTimerId = setTimeout(() => {
            flushPendingLogs();
        }, LOG_BATCH_INTERVAL_MS);
    }
}

function logInfo(line) {
    logEmit("I:" + line);
}

function logError(line) {
    logEmit("E:" + line);
}

function flushPendingLogs() {
    if (pendingLogLines.length === 0) {
        if (logBatchTimerId !== null) {
            clearTimeout(logBatchTimerId);
            logBatchTimerId = null;
        }
        return;
    }

    const lines = pendingLogLines;
    pendingLogLines = [];
    if (logBatchTimerId !== null) {
        clearTimeout(logBatchTimerId);
        logBatchTimerId = null;
    }
    self.postMessage({ type: "log", data: { lines } });
}

function bytesToHex(bytes) {
    return Array.from(bytes, (b) => b.toString(16).padStart(2, "0")).join("");
}

async function installIfcOpenShell(micropip) {
    const response = await fetch(IFCOPENSHELL_WHEEL_URL);
    if (!response.ok) {
        throw new Error(`ifcopenshellのダウンロードに失敗しました: ${response.status}`);
    }
    const wheelBuffer = await response.arrayBuffer();
    const digest = await crypto.subtle.digest("SHA-256", wheelBuffer);
    const digestHex = bytesToHex(new Uint8Array(digest));
    if (digestHex !== IFCOPENSHELL_WHEEL_SHA256) {
        throw new Error("ifcopenshellのハッシュ検証に失敗しました。");
    }
    try {
        pyodide.FS.writeFile(IFCOPENSHELL_PATH, new Uint8Array(wheelBuffer));
        await micropip.install("emfs:" + IFCOPENSHELL_PATH);
    } finally {
        try {
            pyodide.FS.unlink(IFCOPENSHELL_PATH);
        } catch { }
    }
}

async function loadPython(stbkitVersion) {
    if (loadedPython) {
        return;
    }

    logInfo("Python環境の読み込み開始");
    pyodide = await loadPyodide({
        stdout: (line) => logEmit(String(line)),
        stderr: (line) => logEmit(String(line)),
    });
    logInfo("Python環境の読み込みが完了");

    logInfo("micropipパッケージの読み込み開始");
    await pyodide.loadPackage("micropip");
    const micropip = pyodide.pyimport("micropip");
    try {
        logInfo("micropipパッケージの読み込みが完了");

        logInfo(`stbkitパッケージ(v${stbkitVersion})の読み込み開始`);
        await micropip.install(`${STBKIT_PACKAGE_NAME}==${stbkitVersion}`);
        logInfo("stbkitパッケージの読み込みが完了");

        logInfo("ifcopenshellパッケージの読み込み開始");
        await installIfcOpenShell(micropip);
        logInfo("ifcopenshellパッケージの読み込みが完了");
    } finally {
        micropip.destroy();
    }

    logInfo("Pythonスクリプトの読み込み開始");
    await pyodide.runPythonAsync(CONVERT_SRC);
    logInfo("Pythonスクリプトの読み込み完了");
    loadedPython = true;
}

function convertToIfc(inputBytes) {
    if (!loadedPython) {
        throw new Error("Python環境が初期化されていません。");
    }

    pyodide.FS.writeFile(INPUT_PATH, new Uint8Array(inputBytes));
    const converter = pyodide.globals.get("stbkit_convert_to_ifc");
    try {
        return converter(INPUT_PATH);
    } finally {
        converter.destroy();
        try {
            pyodide.FS.unlink(INPUT_PATH);
        } catch { }
    }
}

self.addEventListener("message", async (event) => {
    const { id, type, data } = event.data;

    try {
        if (type === "init") {
            await loadPython(data.stbkitVersion);
            flushPendingLogs();
            self.postMessage({ id, type: "eventResult", result: "ok", data: { initialized: true } });
            return;
        }

        if (type === "convertToIfc") {
            const ifcText = convertToIfc(data.inputBytes);
            flushPendingLogs();
            self.postMessage({ id, type: "eventResult", result: "ok", data: { ifcText } });
            return;
        }

        throw new Error(`未知のジョブです: ${String(type)}`);
    } catch (error) {
        flushPendingLogs();
        const message = error instanceof Error ? error.message : String(error);
        self.postMessage({ id, type: "eventResult", result: "error", data: { message } });
    }
});
