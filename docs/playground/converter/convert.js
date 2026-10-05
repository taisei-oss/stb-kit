// Copyright 2026 TAISEI CORPORATION
// SPDX-License-Identifier: MPL-2.0
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

const STBKIT_VERSION = "0.1.0b3";
const WORKER_SCRIPT_PATH = "./convert.worker.js";

let worker = null;
let workerObjectUrl = null;
let nextRequestId = 0;
const pendingRequests = new Map();
let loadedPython = false;
let downloadUrl = null;

function logEmit(line) {
    const logTextArea = document.getElementById('logTextArea');
    logTextArea.value += line + "\n";
    logTextArea.scrollTop = logTextArea.scrollHeight;
}

function logEmitLines(lines) {
    if (lines.length === 0) {
        return;
    }
    const logTextArea = document.getElementById('logTextArea');
    logTextArea.value += lines.join("\n") + "\n";
    logTextArea.scrollTop = logTextArea.scrollHeight;
}

function logInfo(line) {
    logEmit("I:" + line);
}

function logError(line) {
    logEmit("E:" + line);
}

function logException(error, preMessage = "") {
    console.error(error);
    let message = error instanceof Error ? error.message : String(error);
    if (preMessage) {
        message = preMessage + ": " + message;
    }
    logError(message);
}

async function createWorker() {
    const response = await fetch(WORKER_SCRIPT_PATH);
    if (!response.ok) {
        throw new Error(`Workerの読み込みに失敗しました: ${response.status}`);
    }

    const source = await response.text();
    workerObjectUrl = URL.createObjectURL(
        new Blob([source], { type: "text/javascript" }),
    );
    return new Worker(workerObjectUrl);
}

function deleteWorker() {
    if (worker !== null) {
        worker.terminate();
        worker = null;
    }
    if (workerObjectUrl !== null) {
        URL.revokeObjectURL(workerObjectUrl);
        workerObjectUrl = null;
    }
}

async function ensureWorker() {
    if (worker !== null) {
        return;
    }

    const createdWorker = await createWorker();
    createdWorker.addEventListener("message", (event) => {
        const { id, type, result, data } = event.data;

        if (type === "log") {
            logEmitLines(Array.isArray(data?.lines) ? data.lines : []);
            return;
        }

        const pending = pendingRequests.get(id);
        if (!pending) {
            return;
        }

        pendingRequests.delete(id);
        if (result === "ok") {
            pending.resolve(data);
        } else {
            pending.reject(new Error(data?.message ?? "Workerエラー"));
        }
    });

    createdWorker.addEventListener("error", (event) => {
        const message = event.message || "Workerの実行中にエラーが発生しました。";
        for (const pending of pendingRequests.values()) {
            pending.reject(new Error(message));
        }
        pendingRequests.clear();
        deleteWorker();
    });

    worker = createdWorker;
}

async function callWorker(type, data = {}, transfer = []) {
    await ensureWorker();

    const id = ++nextRequestId;
    return new Promise((resolve, reject) => {
        pendingRequests.set(id, { resolve, reject });
        worker.postMessage({ id, type, data }, transfer);
    });
}

async function loadPython() {
    if (loadedPython) {
        return;
    }

    try {
        await callWorker("init", { stbkitVersion: STBKIT_VERSION });
        document.getElementById("stbkit-version").textContent = STBKIT_VERSION;
        const inputArea = document.getElementById('input-area');
        inputArea.hidden = false;
        const loadingMessage = document.getElementById('loading-message');
        loadingMessage.textContent = "初期化が完了しました。";
        loadedPython = true;
    } catch (error) {
        const loadingMessage = document.getElementById('loading-message');
        loadingMessage.textContent =
            "初期化に失敗しました。ネットワーク接続を確認してページを再読み込みしてください。";
        logException(error, "環境構築エラー");
    }
}

function clearDownloadLink() {
    const link = document.getElementById("download");
    if (downloadUrl !== null) {
        URL.revokeObjectURL(downloadUrl);
        downloadUrl = null;
    }
    link.hidden = true;
    link.removeAttribute("href");
    link.removeAttribute("download");
    link.textContent = "";
}

function createDownloadLink(text, downloadFileName) {
    const link = document.getElementById("download");
    downloadUrl = URL.createObjectURL(
        new Blob([text], { type: "text/plain;charset=utf-8" }),
    );
    link.href = downloadUrl;
    link.download = downloadFileName;
    link.textContent = `${downloadFileName} をダウンロード`;
    link.hidden = false;
}

async function convertToIfc() {
    clearDownloadLink();

    const file = document.getElementById("input-file").files?.[0];
    if (!file) {
        logError("ST-Bridgeファイルが選択されていません。");
        return;
    }

    logInfo(`${file.name}をIFCへ変換しています`);
    const inputBytes = await file.arrayBuffer();
    const result = await callWorker(
        "convertToIfc",
        { inputBytes },
        [inputBytes],
    );

    const downloadFileName = file.name.replace(/\.(stb|xml)$/i, "") + ".ifc";
    createDownloadLink(result.ifcText, downloadFileName);
    logInfo("変換完了");
}

async function initializeButtonToIfc() {
    const convertButton = document.getElementById("convert-ifc");
    const inputFile = document.getElementById("input-file");
    inputFile.addEventListener("change", () => {
        clearDownloadLink();
    });

    convertButton.addEventListener("click", async () => {
        convertButton.disabled = true;
        inputFile.disabled = true;
        try {
            await convertToIfc();
        } catch (error) {
            logException(error, "変換エラー");
        } finally {
            inputFile.disabled = false;
            convertButton.disabled = false;
        }
    });
}

document.addEventListener("DOMContentLoaded", async () => {
    await loadPython();
    await initializeButtonToIfc();
});

window.addEventListener("beforeunload", () => {
    deleteWorker();
});
