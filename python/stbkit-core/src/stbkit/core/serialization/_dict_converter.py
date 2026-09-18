# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from collections.abc import Mapping, Sequence
from datetime import date, datetime
from enum import Enum
from logging import Logger
from pathlib import Path
from typing import Any, Never, overload
from uuid import UUID

from .._internal.constants import SUPPORTED_STB_VERSIONS
from .._internal.extension_utils import ExtensionInfoRepository
from .._internal.name_converter import (
    private_field_name,
    snake_case_to_lower_camel_case,
    xml_element_name_to_key,
)
from .._internal.xml_value_converter import any_to_xml_str
from ..data_model._internal.stb_types import DataType
from ..data_model.common import (
    StBridgeElement,
    StBridgeRoot,
    _FieldInfo,
    _FieldKind,
    _InvalidValue,
    _StBridgeExtensionElement,
)
from ..stb_exceptions import SchemaError, UnsupportedStbVersionError
from ..stb_io._internal.stream_reader import _get_module
from ..stb_reporting import Code, Phase, Reporter, get_reporter
from .config import DictProfile, KeyStyle, ValueStyle
from .profiles import _XMLTODICT_COMPAT, DEFAULT


def _root_type_by_version(version: str) -> type[StBridgeRoot]:
    module = _get_module(version)
    root_type = getattr(module, "StBridge", None)
    if not isinstance(root_type, type) or not issubclass(root_type, StBridgeRoot):
        raise UnsupportedStbVersionError(version)
    return root_type


def to_dict(
    element: StBridgeElement,
    *,
    _profile: DictProfile = DEFAULT,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> dict[str, Any]:
    """ST-Bridge要素を辞書へ変換します。

    ルート要素以外も変換できます。
    モデル内のリストや辞書は複製します。
    辞書を変更しても、入力モデルには影響しません。

    Args:
        element: 変換するST-Bridgeの要素。
        _profile: 辞書の変換ルール。検証中のため、指定せず既定値を使用してください。
        logger: 出力先Logger。
        reporter: 出力先Reporter。

    Returns:
        dict[str, Any]: ST-Bridgeの辞書。

    Raises:
        TypeError: フィールドの値がモデルの型定義と一致しない場合。
        ValueError: 要素が循環参照している場合、辞書キーが衝突した場合、
            または要素のからバージョン解決ができない場合。

    Examples:
        >>> import stbkit.api
        >>> raw = stbkit.api.experimental.to_dict(stb)
    """
    reporter = get_reporter(logger, reporter)

    result: dict[str, Any] = _element_to_dict(
        element,
        profile=_profile,
        reporter=reporter,
        path=element._xml_name(),
        active_element_ids=set(),
    )
    if _profile.wrap_root and isinstance(element, StBridgeRoot):
        return {_external_element_name(element._xml_name(), _profile): result}
    return result


@overload
def from_dict[T: StBridgeRoot](
    data: Mapping[str, Any],
    *,
    root_type: type[T],
    _profile: DictProfile = DEFAULT,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> T: ...


@overload
def from_dict(
    data: Mapping[str, Any],
    *,
    root_type: None = None,
    _profile: DictProfile = DEFAULT,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> StBridgeRoot: ...


def from_dict(
    data: Mapping[str, Any],
    *,
    root_type: type[StBridgeRoot] | None = None,
    _profile: DictProfile = DEFAULT,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> StBridgeRoot:
    """辞書からST-Bridgeのモデルへの変換。

    値不正はloadと同様に、不正値等は退避しつつ、可能な範囲で読み込みます。

    root_typeを指定した場合は、その型に読み込みます。
    root_typeを省略した場合は、辞書のversionから読み込む型を判断します。

    Args:
        data: 読み込む辞書。
        root_type: 戻り値の型。Noneの場合はdataのversionから決定します。
        _profile: 辞書の変換ルール。検証中のため指定せず規定値を利用してください。
        logger: 出力先Logger
        reporter: 出力先Reporter。

    Returns:
        StBridgeRoot: ST-Bridgeモデル。

    Raises:
        SchemaError: `root_type`を省略したときに、辞書にversionが無い場合、
            versionを一意に決定できない場合、または値が不正な場合。
        UnsupportedStbVersionError: `root_type`を省略したときに、
            対応していないバージョンが指定された場合。
        ValueError: 入力の辞書が循環参照している場合、または同じフィールドへ
            対応する辞書キーが衝突した場合。

    Examples:
        >>> import stbkit.api as api
        >>> stb_dict = api.experimental.to_dict(stb)
        >>> new_stb = api.experimental.from_dict(stb_dict)
    """
    reporter = get_reporter(logger, reporter)
    if root_type and not issubclass(root_type, StBridgeRoot):
        raise TypeError("root_typeはStBridgeRootを継承している必要があります")

    explicit_root: StBridgeRoot | None = None
    if root_type is not None:
        explicit_root = root_type()

    root_data, wrapper_key = _unwrap_root(
        data,
        profile=_profile,
        reporter=reporter,
        root=explicit_root,
    )

    selected_version: str | None = None
    if explicit_root is None:
        selected_version = _read_version(
            root_data,
            profile=_profile,
            reporter=reporter,
        )
        stb = _root_type_by_version(selected_version)()
    else:
        stb = explicit_root

    _validate_root_wrapper(
        wrapper_key,
        stb,
        profile=_profile,
        reporter=reporter,
    )

    _element_from_dict(
        root_data,
        stb,
        profile=_profile,
        reporter=reporter,
        path=stb._xml_name(),
        active_mapping_ids=set(),
    )

    loaded_version = getattr(stb, "version_or_none", None)
    if selected_version is not None and loaded_version != selected_version:
        reporter.error(
            message="辞書のversionをモデルへ設定できませんでした",
            code=Code.VERSION_MISMATCH,
            phase=Phase.LOAD,
            value=None if loaded_version is None else str(loaded_version),
            ref_value=selected_version,
            stb_element=stb,
            attr_name="version",
        )

    # loadと同様にバリデーションと拡張修復を行う。
    # validatorはstb_ioも参照するため、循環インポートを避けてここでimportする。
    from ..validation._internal.validator import _validate

    _validate(reporter=reporter, stb=stb)
    ext_repo: ExtensionInfoRepository = ExtensionInfoRepository()
    ext_repo.register(stb, reporter=reporter, phase=Phase.LOAD)
    ext_repo.repair_stb(stb, reporter=reporter, phase=Phase.LOAD)
    return stb


def _resolve_model_version(
    element_or_type: StBridgeElement | type[StBridgeElement],
) -> str:
    if isinstance(element_or_type, type):
        element_type = element_or_type
        element: StBridgeElement | None = None
    else:
        element_type = type(element_or_type)
        element = element_or_type

    # 拡張子要素はcommonで定義されるため、
    # 親要素をたどって最初に見つかったVERSIONを使用する。
    if issubclass(element_type, _StBridgeExtensionElement):
        if element is None:
            raise ValueError(
                "拡張子要素型だけではバージョンを解決できません。"
                "親を持つインスタンスを指定してください"
            )

        current = element._parent
        while current is not None:
            version = type(current)._try_get_module_version()
            if version is not None:
                return version
            current = current._parent

        raise ValueError("親から拡張子要素のバージョンを解決できません")

    # 通常要素は、各クラスの定義モジュールにあるVERSIONを使用。
    # (1つのデータモデルに異なるバージョンのモジュールが混在する場合の対策)
    version = element_type._try_get_module_version()
    if version is None:
        module_name = element_type.__module__
        raise ValueError(f"モデルのモジュールにVERSION定数がありません: {module_name}")
    return version


def _should_omit_value(value: Any, profile: DictProfile) -> bool:
    """省略する値か判定

    omit_noneはNoneだけが対象。
    omit_emptyはNone、空のMapping、空のlistが対象。空文字列、0、False、空tupleは省略しない。
    """
    if value is None:
        return profile.omit_none or profile.omit_empty
    if not profile.omit_empty:
        return False
    if isinstance(value, Mapping):
        return len(value) == 0
    return isinstance(value, list) and len(value) == 0


def _element_to_dict(
    element: StBridgeElement,
    *,
    profile: DictProfile,
    reporter: Reporter,
    path: str,
    active_element_ids: set[int],
) -> dict[str, Any]:
    try:
        _resolve_model_version(element)
    except ValueError as error:
        reporter.error(
            message=str(error),
            code=Code.VERSION_UNSUPPORTED,
            phase=Phase.DUMP,
            stb_element=element,
        )
        raise

    element_id = id(element)
    if element_id in active_element_ids:
        reporter.error(
            message=f"循環参照を検出しました: {path}",
            code=Code.SCHEMA_ERROR,
            phase=Phase.DUMP,
            stb_element=element,
        )
        raise ValueError(f"循環参照を検出しました: {path}")

    active_element_ids.add(element_id)
    try:
        result: dict[str, Any] = {}
        for field_name, field_info in element._fields.items():
            value = getattr(element, private_field_name(field_name))
            if _should_omit_value(value, profile):
                continue

            key = _field_key(element, field_name, field_info, profile)
            field_path = f"{path}.{key}"
            converted = _field_value_to_external(
                value,
                element=element,
                field_name=field_name,
                field_info=field_info,
                profile=profile,
                reporter=reporter,
                path=field_path,
                active_element_ids=active_element_ids,
            )
            if _should_omit_value(converted, profile):
                continue
            _put_unique(
                result,
                key,
                converted,
                element=element,
                field_name=field_name,
                path=field_path,
                reporter=reporter,
            )

        _append_extension_data(
            result,
            element=element,
            profile=profile,
            reporter=reporter,
            path=path,
            active_element_ids=active_element_ids,
        )
        return result
    finally:
        active_element_ids.remove(element_id)


def _field_value_to_external(
    value: Any,
    *,
    element: StBridgeElement,
    field_name: str,
    field_info: _FieldInfo,
    profile: DictProfile,
    reporter: Reporter,
    path: str,
    active_element_ids: set[int],
) -> Any:
    if value is None:
        return None

    if field_info.kind is _FieldKind.ELEMENT:
        if field_info.max_occurs == 1:
            if not isinstance(value, StBridgeElement):
                _raise_output_type_error(
                    element,
                    field_name,
                    path,
                    expected="StBridgeElement",
                    actual=value,
                    reporter=reporter,
                )
            return _element_to_dict(
                value,
                profile=profile,
                reporter=reporter,
                path=path,
                active_element_ids=active_element_ids,
            )

        if not isinstance(value, list):
            _raise_output_type_error(
                element,
                field_name,
                path,
                expected="list[StBridgeElement]",
                actual=value,
                reporter=reporter,
            )
        children: list[dict[str, Any]] = []
        for index, item in enumerate(value):
            if not isinstance(item, StBridgeElement):
                _raise_output_type_error(
                    element,
                    field_name,
                    f"{path}[{index}]",
                    expected="StBridgeElement",
                    actual=item,
                    reporter=reporter,
                )
            children.append(
                _element_to_dict(
                    item,
                    profile=profile,
                    reporter=reporter,
                    path=f"{path}[{index}]",
                    active_element_ids=active_element_ids,
                )
            )
        return children

    if (
        profile.value_style is ValueStyle.XML
        and field_info.kind is _FieldKind.CONTENT
        and isinstance(value, list)
    ):
        return " ".join(_xml_scalar(item) for item in value)
    return _value_to_external(value, profile=profile, reporter=reporter, path=path)


def _append_extension_data(
    result: dict[str, Any],
    *,
    element: StBridgeElement,
    profile: DictProfile,
    reporter: Reporter,
    path: str,
    active_element_ids: set[int],
) -> None:
    extension = element._extension
    if extension is None:
        return

    if extension._attributes:
        for raw_name, value in extension._attributes.items():
            if _should_omit_value(value, profile):
                continue
            key = f"{profile.attribute_prefix}{raw_name}"
            converted = _value_to_external(
                value,
                profile=profile,
                reporter=reporter,
                path=f"{path}.{key}",
            )
            if _should_omit_value(converted, profile):
                continue
            _put_unique(
                result,
                key,
                converted,
                element=element,
                field_name=raw_name,
                path=f"{path}.{key}",
                reporter=reporter,
            )

    if not extension._children:
        return

    grouped: dict[str, list[dict[str, Any]]] = {}
    for index, child in enumerate(extension._children):
        raw_name = child._xml_name()
        key = f"{profile.child_prefix}{raw_name}"
        child_result = _element_to_dict(
            child,
            profile=profile,
            reporter=reporter,
            path=f"{path}.{key}[{index}]",
            active_element_ids=active_element_ids,
        )
        grouped.setdefault(key, []).append(child_result)

    for key, values in grouped.items():
        output_value: dict[str, Any] | list[dict[str, Any]]
        output_value = values[0] if len(values) == 1 else values
        if _should_omit_value(output_value, profile):
            continue
        _put_unique(
            result,
            key,
            output_value,
            element=element,
            field_name=key,
            path=f"{path}.{key}",
            reporter=reporter,
        )


def _put_unique(
    target: dict[str, Any],
    key: str,
    value: Any,
    *,
    element: StBridgeElement,
    field_name: str,
    path: str,
    reporter: Reporter,
) -> None:
    if key in target:
        message = (
            f"{element.__class__.__name__}で辞書キーが衝突しました: "
            f"key={key!r}, field={field_name!r}, path={path}"
        )
        reporter.error(
            message=message,
            code=Code.SCHEMA_ERROR,
            phase=Phase.DUMP,
            stb_element=element,
        )
        raise ValueError(message)
    target[key] = value


def _raise_output_type_error(
    element: StBridgeElement,
    field_name: str,
    path: str,
    *,
    expected: str,
    actual: Any,
    reporter: Reporter,
) -> Never:
    message = f"{path}: expected {expected}, actual {type(actual).__name__}"
    reporter.error(
        message=message,
        code=Code.TYPE_MISMATCH,
        phase=Phase.DUMP,
        stb_element=element,
        attr_name=field_name,
        value=type(actual).__name__,
        ref_value=expected,
    )
    raise TypeError(message)


def _value_to_external(
    value: Any,
    *,
    profile: DictProfile,
    reporter: Reporter,
    path: str,
) -> Any:
    try:
        match profile.value_style:
            case ValueStyle.PYTHON:
                return _python_value(value, profile=profile)
            case ValueStyle.JSON:
                return _json_value(value, profile=profile)
            case ValueStyle.XML:
                return _xml_external_value(value, profile=profile)
    except TypeError as error:
        reporter.error(
            message=f"{path}: {error}",
            code=Code.TYPE_MISMATCH,
            phase=Phase.DUMP,
            value=type(value).__name__,
        )
        raise
    raise AssertionError("到達不能なvalue_styleです")


def _python_value(value: Any, *, profile: DictProfile) -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, item in value.items():
            if _should_omit_value(item, profile):
                continue
            converted = _python_value(item, profile=profile)
            if _should_omit_value(converted, profile):
                continue
            result[_require_string_key(key)] = converted
        return result
    if isinstance(value, list):
        return [_python_value(item, profile=profile) for item in value]
    if isinstance(value, tuple):
        return tuple(_python_value(item, profile=profile) for item in value)
    return value


def _json_value(value: Any, *, profile: DictProfile) -> Any:
    if value is None:
        return None
    if isinstance(value, Enum):
        return _json_value(value.value, profile=profile)
    if isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, UUID):
        return str(value)
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, item in value.items():
            if _should_omit_value(item, profile):
                continue
            converted = _json_value(item, profile=profile)
            if _should_omit_value(converted, profile):
                continue
            result[_require_string_key(key)] = converted
        return result
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [_json_value(item, profile=profile) for item in value]
    type_name = type(value).__name__
    raise TypeError(f"JSONへ変換できない型です: {type_name}")


def _xml_external_value(value: Any, *, profile: DictProfile) -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, item in value.items():
            if _should_omit_value(item, profile):
                continue
            converted = _xml_external_value(item, profile=profile)
            if _should_omit_value(converted, profile):
                continue
            result[_require_string_key(key)] = converted
        return result
    if isinstance(value, list):
        return [_xml_external_value(item, profile=profile) for item in value]
    return _xml_value(value)


def _xml_value(value: Any) -> str | None:
    if value is None:
        return None
    return _xml_scalar(value)


def _xml_scalar(value: Any) -> str:
    return any_to_xml_str(value)


def _require_string_key(key: Any) -> str:
    if not isinstance(key, str):
        type_name = type(key).__name__
        message = f"辞書キーはstrである必要があります: {type_name}"
        raise TypeError(message)
    return key


def _field_key(
    element: StBridgeElement,
    field_name: str,
    field_info: _FieldInfo,
    profile: DictProfile,
) -> str:
    if field_info.kind is _FieldKind.CONTENT:
        return profile.content_key

    match profile.key_style:
        case KeyStyle.XML:
            external_name = element._xml_name(field_name)
        case KeyStyle.SNAKE:
            external_name = field_name
        case KeyStyle.CAMEL:
            external_name = snake_case_to_lower_camel_case(field_name)
        case _:
            raise AssertionError("到達不能なkey_styleです")

    if field_info.kind is _FieldKind.ATTRIBUTE:
        return f"{profile.attribute_prefix}{external_name}"
    return f"{profile.child_prefix}{external_name}"


def _external_element_name(xml_name: str, profile: DictProfile) -> str:
    match profile.key_style:
        case KeyStyle.XML:
            return xml_name
        case KeyStyle.SNAKE:
            return xml_element_name_to_key(xml_name)
        case KeyStyle.CAMEL:
            return snake_case_to_lower_camel_case(xml_element_name_to_key(xml_name))
    raise AssertionError("到達不能なkey_styleです")


def _unwrap_root(
    data: Mapping[Any, Any],
    *,
    profile: DictProfile,
    reporter: Reporter,
    root: StBridgeRoot | None,
) -> tuple[Mapping[Any, Any], object | None]:
    """ルート内容と、入力に含まれていたらキーを返す。

    root=Noneの場合、この時点ではversionが未確定のため、ルート型が選択できない。
    そのため要素名は検証せず、ラップ解除のみ行う。
    ルート型が明示されている場合は、ルート要素名もラップ検出に利用する。
    """
    if profile.omit_none or profile.omit_empty:
        data = {
            key: value
            for key, value in data.items()
            if not _should_omit_value(value, profile)
        }

    if profile.wrap_root:
        if len(data) == 1:
            key, value = next(iter(data.items()))
            if isinstance(value, Mapping):
                return value, key

        reporter.error(
            message="ルートラップの形状がprofileと一致しません",
            code=Code.SCHEMA_ERROR,
            phase=Phase.LOAD,
        )
        if root is not None:
            wrapped = _find_model_root_wrapper(
                data,
                root=root,
                profile=profile,
            )
            if wrapped is not None:
                return wrapped[1], wrapped[0]
            return data, None
        if _contains_version_key(data, profile=profile):
            return data, None
        wrapped = _find_wrapped_root(data, profile=profile)
        if wrapped is not None:
            return wrapped[1], wrapped[0]
        return data, None
    if root is not None:
        wrapped = None
        if len(data) == 1:
            wrapped = _find_model_root_wrapper(
                data,
                root=root,
                profile=profile,
            )
        if wrapped is not None:
            key, value = wrapped
            reporter.error(
                message=(
                    "ルートがラップされていますが、"
                    f"profile.wrap_rootはFalseです: key={key!r}"
                ),
                code=Code.SCHEMA_ERROR,
                phase=Phase.LOAD,
            )
            return value, key
        return data, None
    if _contains_version_key(data, profile=profile):
        return data, None

    wrapped = _find_wrapped_root(data, profile=profile)
    if wrapped is not None:
        key, value = wrapped
        reporter.error(
            message=(
                "ルートがラップされていますが、"
                f"profile.wrap_rootはFalseです: key={key!r}"
            ),
            code=Code.SCHEMA_ERROR,
            phase=Phase.LOAD,
        )
        return value, key
    return data, None


def _find_model_root_wrapper(
    data: Mapping[Any, Any],
    *,
    root: StBridgeRoot,
    profile: DictProfile,
) -> tuple[object, Mapping[Any, Any]] | None:
    expected_key = _external_element_name(root._xml_name(), profile)
    value = data.get(expected_key)
    if isinstance(value, Mapping):
        return expected_key, value
    return None


def _find_wrapped_root(
    data: Mapping[Any, Any],
    *,
    profile: DictProfile,
) -> tuple[object, Mapping[Any, Any]] | None:
    """versionキーを持つトップレベル辞書値を1つだけ検出する。"""
    candidates: list[tuple[object, Mapping[Any, Any]]] = []
    for key, value in data.items():
        if isinstance(value, Mapping) and _contains_version_key(
            value,
            profile=profile,
        ):
            candidates.append((key, value))
    if len(candidates) == 1:
        return candidates[0]
    return None


def _contains_version_key(
    data: Mapping[Any, Any],
    *,
    profile: DictProfile,
) -> bool:
    return any(key in data for key in _version_keys(profile))


def _version_keys(profile: DictProfile) -> tuple[str, ...]:
    """ルート型からversionの外部キー候補を取得する。"""
    result: set[str] = set()
    seen_root_types: set[type[StBridgeRoot]] = set()
    for version in SUPPORTED_STB_VERSIONS:
        root_type = _root_type_by_version(version)
        if root_type in seen_root_types:
            continue
        seen_root_types.add(root_type)
        root = root_type()
        field_info = root._fields.get("version")
        if field_info is None:
            continue
        result.add(_field_key(root, "version", field_info, profile))
    return tuple(sorted(result))


def _validate_root_wrapper(
    wrapper_key: object | None,
    root: StBridgeRoot,
    *,
    profile: DictProfile,
    reporter: Reporter,
) -> None:
    expected_key = _external_element_name(root._xml_name(), profile)

    if profile.wrap_root:
        if wrapper_key is None:
            reporter.error(
                message=(f"ルートがラップされていません。期待キー: {expected_key!r}"),
                code=Code.SCHEMA_ERROR,
                phase=Phase.LOAD,
            )
            return
        if wrapper_key != expected_key:
            reporter.error(
                message=(
                    "ルート要素名がモデルと一致しません: "
                    f"expected={expected_key!r}, actual={wrapper_key!r}"
                ),
                code=Code.SCHEMA_ERROR,
                phase=Phase.LOAD,
            )
        return


def _read_version(
    data: Mapping[Any, Any],
    *,
    profile: DictProfile,
    reporter: Reporter,
) -> str:
    version_keys = _version_keys(profile)
    present_keys = [key for key in version_keys if key in data]
    if not present_keys:
        reporter.error(
            message=f"辞書にversionが含まれません: keys={list(version_keys)!r}",
            code=Code.SCHEMA_ERROR,
            phase=Phase.LOAD,
        )
        raise SchemaError("辞書にversionが含まれません")

    version_key = present_keys[0]
    if len(present_keys) > 1:
        values = {str(data[key]) for key in present_keys}
        if len(values) > 1:
            reporter.error(
                message=(
                    "複数のversionキーに異なる値が指定されています: "
                    f"keys={present_keys!r}"
                ),
                code=Code.VERSION_MISMATCH,
                phase=Phase.LOAD,
            )
            raise SchemaError("辞書のversionを一意に決定できません")
        reporter.error(
            message=f"複数のversionキーが指定されています: keys={present_keys!r}",
            code=Code.SCHEMA_ERROR,
            phase=Phase.LOAD,
        )

    raw_version = data[version_key]
    if raw_version is None:
        reporter.error(
            message=f"辞書のversionがnullです: key={version_key!r}",
            code=Code.SCHEMA_ERROR,
            phase=Phase.LOAD,
        )
        raise SchemaError("辞書にversionが含まれません")
    if isinstance(raw_version, (Mapping, list, tuple, set)):
        reporter.error(
            message="versionの値が不正です",
            code=Code.TYPE_MISMATCH,
            phase=Phase.LOAD,
            value=type(raw_version).__name__,
            ref_value="str",
        )
        raise SchemaError("versionの値が不正です")

    version = str(raw_version)
    if version not in SUPPORTED_STB_VERSIONS:
        reporter.error(
            message=f"未対応のST-Bridgeバージョンです: {version}",
            code=Code.VERSION_UNSUPPORTED,
            phase=Phase.LOAD,
            value=version,
        )
        raise UnsupportedStbVersionError(version)
    return version


def _element_from_dict[TElement: StBridgeElement](
    data: Mapping[Any, Any],
    element: TElement,
    *,
    profile: DictProfile,
    reporter: Reporter,
    path: str,
    active_mapping_ids: set[int],
) -> TElement:
    mapping_id = id(data)
    if mapping_id in active_mapping_ids:
        reporter.error(
            message=f"入力辞書の循環参照を検出しました: {path}",
            code=Code.SCHEMA_ERROR,
            phase=Phase.LOAD,
            stb_element=element,
        )
        raise ValueError(f"入力辞書の循環参照を検出しました: {path}")

    active_mapping_ids.add(mapping_id)
    try:
        key_map = _external_key_to_field(element, profile=profile, reporter=reporter)
        for raw_key, value in data.items():
            if _should_omit_value(value, profile):
                continue
            if not isinstance(raw_key, str):
                _store_invalid_value(
                    element,
                    kind=_FieldKind.ATTRIBUTE,
                    value={raw_key: value},
                    xml_path=element._path_xml(),
                    dict_path=path,
                    reason="辞書キーがstrではありません",
                    reporter=reporter,
                )
                continue

            field_name = key_map.get(raw_key)
            if field_name is None:
                _read_unknown_key(
                    element,
                    raw_key,
                    value,
                    profile=profile,
                    reporter=reporter,
                    path=f"{path}.{raw_key}",
                    active_mapping_ids=active_mapping_ids,
                )
                continue

            field_info = element._field_info(field_name)
            field_path = f"{path}.{raw_key}"
            if field_info.kind is _FieldKind.ELEMENT:
                _read_child_value(
                    element,
                    field_name,
                    field_info,
                    value,
                    profile=profile,
                    reporter=reporter,
                    path=field_path,
                    active_mapping_ids=active_mapping_ids,
                )
            else:
                _read_scalar_value(
                    element,
                    field_name,
                    field_info,
                    value,
                    profile=profile,
                    reporter=reporter,
                    path=field_path,
                )
        return element
    finally:
        active_mapping_ids.remove(mapping_id)


def _external_key_to_field(
    element: StBridgeElement,
    *,
    profile: DictProfile,
    reporter: Reporter,
) -> dict[str, str]:
    result: dict[str, str] = {}
    for field_name, field_info in element._fields.items():
        key = _field_key(element, field_name, field_info, profile)
        previous = result.get(key)
        if previous is not None:
            message = (
                f"{element.__class__.__name__}の逆引きキーが衝突しました: "
                f"key={key!r}, fields=({previous!r}, {field_name!r})"
            )
            reporter.error(
                message=message,
                code=Code.SCHEMA_ERROR,
                phase=Phase.LOAD,
                stb_element=element,
            )
            raise ValueError(message)
        result[key] = field_name
    return result


def _read_scalar_value(
    element: StBridgeElement,
    field_name: str,
    field_info: _FieldInfo,
    value: Any,
    *,
    profile: DictProfile,
    reporter: Reporter,
    path: str,
) -> None:
    if field_info.kind is _FieldKind.CONTENT:
        _read_content_value(
            element,
            field_name,
            field_info,
            value,
            profile=profile,
            reporter=reporter,
            path=path,
        )
        return

    before = _invalid_value_count(element)
    try:
        if value is None:
            element._set_attribute_by_any(field_name, None)
        elif field_info.data_type is DataType.INT_ENUM:
            enum_value = _to_int_enum_value(element, field_name, field_info, value)
            element._set_attribute_by_any(field_name, enum_value)
        elif profile.value_style is ValueStyle.XML:
            if not isinstance(value, str):
                raise TypeError("XMLの属性はstrで指定してください")
            element._set_attribute_by_str(
                field_name,
                value,
                raw_attr_name=element._xml_name(field_name),
            )
        else:
            element._set_attribute_by_any(field_name, value)
    except (SchemaError, TypeError, ValueError) as error:
        if _invalid_value_count(element) == before:
            setattr(element, private_field_name(field_name), None)
            _store_invalid_value(
                element,
                kind=field_info.kind,
                value=value,
                xml_path=_field_xml_path(element, field_name, field_info),
                dict_path=path,
                reason=str(error),
                reporter=reporter,
            )
        return

    _report_new_invalid_values(
        element,
        start_index=before,
        dict_path=path,
        reporter=reporter,
    )


def _read_content_value(
    element: StBridgeElement,
    field_name: str,
    field_info: _FieldInfo,
    value: Any,
    *,
    profile: DictProfile,
    reporter: Reporter,
    path: str,
) -> None:
    try:
        normalized = value
        if profile.value_style is ValueStyle.XML and value is not None:
            if not isinstance(value, str):
                raise TypeError("XMLの内容はstrで指定してください")
            if field_info.data_type in (
                DataType.MONOLIST,
                DataType.MONOLIST_ID,
                DataType.POSITIVE_INTEGER_LIST,
            ):
                normalized = [int(item) for item in value.split()]
            elif field_info.data_type is DataType.MONOLIST_LENGTH:
                normalized = [float(item) for item in value.split()]
        setattr(element, field_name, normalized)
    except (SchemaError, TypeError, ValueError) as error:
        setattr(element, private_field_name(field_name), None)
        _store_invalid_value(
            element,
            kind=_FieldKind.CONTENT,
            value=value,
            xml_path=element._path_xml(),
            dict_path=path,
            reason=str(error),
            reporter=reporter,
        )


def _to_int_enum_value(
    element: StBridgeElement,
    field_name: str,
    field_info: _FieldInfo,
    value: Any,
) -> Enum:
    enum_type = field_info.py_type
    if not isinstance(enum_type, type) or not issubclass(enum_type, Enum):
        raise TypeError(
            f"{element.__class__.__name__}.{field_name}のEnum型情報が不正です"
        )
    normalized = int(value) if isinstance(value, str) else value
    try:
        result = enum_type(normalized)
    except (TypeError, ValueError):
        raise SchemaError(
            f"{enum_type.__name__}に変換できない値です: {value}",
            element=element,
            attr_name=field_name,
        ) from None
    return result


def _read_child_value(
    element: StBridgeElement,
    field_name: str,
    field_info: _FieldInfo,
    value: Any,
    *,
    profile: DictProfile,
    reporter: Reporter,
    path: str,
    active_mapping_ids: set[int],
) -> None:
    if value is None:
        return

    child_type = _child_type(element, field_name, field_info)
    if field_info.max_occurs == 1:
        if isinstance(value, list):
            if not value:
                return
            first, *excess = value
            if not isinstance(first, Mapping):
                _store_invalid_value(
                    element,
                    kind=_FieldKind.ELEMENT,
                    value=value,
                    xml_path=_field_xml_path(element, field_name, field_info),
                    dict_path=path,
                    reason="単一子要素にはMappingが必要です",
                    reporter=reporter,
                )
                return
            child = child_type()
            setattr(element, field_name, child)
            _element_from_dict(
                first,
                child,
                profile=profile,
                reporter=reporter,
                path=f"{path}[0]",
                active_mapping_ids=active_mapping_ids,
            )
            for index, extra in enumerate(excess, start=1):
                _store_invalid_value(
                    element,
                    kind=_FieldKind.ELEMENT,
                    value=extra,
                    xml_path=_field_xml_path(element, field_name, field_info),
                    dict_path=f"{path}[{index}]",
                    reason=(
                        f"要素[{field_name}]の最大回数"
                        f"[{field_info.max_occurs}]を超過しています"
                    ),
                    reporter=reporter,
                )
            return
        if not isinstance(value, Mapping):
            _store_invalid_value(
                element,
                kind=_FieldKind.ELEMENT,
                value=value,
                xml_path=_field_xml_path(element, field_name, field_info),
                dict_path=path,
                reason="単一子要素にはMappingが必要です",
                reporter=reporter,
            )
            return
        child = child_type()
        setattr(element, field_name, child)
        _element_from_dict(
            value,
            child,
            profile=profile,
            reporter=reporter,
            path=path,
            active_mapping_ids=active_mapping_ids,
        )
        return

    values: list[Any]
    if isinstance(value, list):
        values = value
    elif isinstance(value, Mapping) and profile == _XMLTODICT_COMPAT:
        # xmltodict.parse()は、同名要素が1件だとリストを解除するため、
        # 互換プロファイルに限り、1件リストへ正規化する。
        values = [value]
    else:
        _store_invalid_value(
            element,
            kind=_FieldKind.ELEMENT,
            value=value,
            xml_path=_field_xml_path(element, field_name, field_info),
            dict_path=path,
            reason="複数子要素にはlistが必要です",
            reporter=reporter,
        )
        return

    target = getattr(element, private_field_name(field_name))
    if not isinstance(target, list):
        class_name = element.__class__.__name__
        raise TypeError(f"{class_name}.{field_name}の内部値がlistではありません")
    max_occurs = field_info.max_occurs
    for index, item in enumerate(values):
        item_path = f"{path}[{index}]"
        if max_occurs is not None and index >= max_occurs:
            _store_invalid_value(
                element,
                kind=_FieldKind.ELEMENT,
                value=item,
                xml_path=(
                    f"{element._path_xml()}/"
                    f"{element._xml_name(field_name)}[{index + 1}]"
                ),
                dict_path=item_path,
                reason=(
                    f"要素[{field_name}]の最大回数"
                    f"[{field_info.max_occurs}]を超過しています"
                ),
                reporter=reporter,
            )
            continue
        if not isinstance(item, Mapping):
            _store_invalid_value(
                element,
                kind=_FieldKind.ELEMENT,
                value=item,
                xml_path=(
                    f"{element._path_xml()}/"
                    f"{element._xml_name(field_name)}[{index + 1}]"
                ),
                dict_path=item_path,
                reason="子要素の各項目にはMappingが必要です",
                reporter=reporter,
            )
            continue
        child = child_type()
        target.append(child)
        _element_from_dict(
            item,
            child,
            profile=profile,
            reporter=reporter,
            path=item_path,
            active_mapping_ids=active_mapping_ids,
        )


def _child_type(
    element: StBridgeElement,
    field_name: str,
    field_info: _FieldInfo,
) -> type[StBridgeElement]:
    return type(element)._child_class(field_name)


def _read_unknown_key(
    element: StBridgeElement,
    key: str,
    value: Any,
    *,
    profile: DictProfile,
    reporter: Reporter,
    path: str,
    active_mapping_ids: set[int],
) -> None:
    kind = _unknown_key_kind(key, value, profile)
    if kind is _FieldKind.CONTENT:
        _store_invalid_value(
            element,
            kind=kind,
            value=value,
            xml_path=element._path_xml(),
            dict_path=path,
            reason=("内容を持たない要素に内容が指定されています"),
            reporter=reporter,
        )
        return

    if kind is _FieldKind.ATTRIBUTE:
        raw_name = _strip_prefix(key, profile.attribute_prefix)
        if raw_name.startswith("xmlns"):
            return
        element._ensure_extension._set_attribute(raw_name, value)
        return

    raw_name = _strip_prefix(key, profile.child_prefix)
    _read_unknown_child(
        element,
        raw_name,
        value,
        profile=profile,
        reporter=reporter,
        path=path,
        active_mapping_ids=active_mapping_ids,
    )


def _unknown_key_kind(key: str, value: Any, profile: DictProfile) -> _FieldKind:
    if key == profile.content_key:
        return _FieldKind.CONTENT
    if profile.attribute_prefix and key.startswith(profile.attribute_prefix):
        return _FieldKind.ATTRIBUTE
    if profile.child_prefix and key.startswith(profile.child_prefix):
        return _FieldKind.ELEMENT
    if profile.attribute_prefix and not profile.child_prefix:
        return _FieldKind.ELEMENT
    if profile.child_prefix and not profile.attribute_prefix:
        return _FieldKind.ATTRIBUTE
    if isinstance(value, (Mapping, list)):
        return _FieldKind.ELEMENT
    return _FieldKind.ATTRIBUTE


def _read_unknown_child(
    element: StBridgeElement,
    raw_name: str,
    value: Any,
    *,
    profile: DictProfile,
    reporter: Reporter,
    path: str,
    active_mapping_ids: set[int],
) -> None:
    if value is None:
        return
    values = value if isinstance(value, list) else [value]
    for index, item in enumerate(values):
        item_path = path if not isinstance(value, list) else f"{path}[{index}]"
        if not isinstance(item, Mapping):
            _store_invalid_value(
                element,
                kind=_FieldKind.ELEMENT,
                value=item,
                xml_path=f"{element._path_xml()}/{raw_name}",
                dict_path=item_path,
                reason="未知の子要素にはMappingが必要です",
                reporter=reporter,
            )
            continue
        child = _StBridgeExtensionElement(name=raw_name)
        element._ensure_extension._set_child(child)
        _element_from_dict(
            item,
            child,
            profile=profile,
            reporter=reporter,
            path=item_path,
            active_mapping_ids=active_mapping_ids,
        )


def _strip_prefix(key: str, prefix: str) -> str:
    if prefix and key.startswith(prefix):
        return key[len(prefix) :]
    return key


def _field_xml_path(
    element: StBridgeElement,
    field_name: str,
    field_info: _FieldInfo,
) -> str:
    return element._path_xml(field_name)


def _invalid_value_count(element: StBridgeElement) -> int:
    extension = element._extension
    if extension is None or extension._invalid_values is None:
        return 0
    return len(extension._invalid_values)


def _report_new_invalid_values(
    element: StBridgeElement,
    *,
    start_index: int,
    dict_path: str,
    reporter: Reporter,
) -> None:
    extension = element._extension
    if extension is None or extension._invalid_values is None:
        return
    for invalid in extension._invalid_values[start_index:]:
        reporter.error(
            message=f"{dict_path}: {invalid.reason}",
            code=Code.SCHEMA_ERROR,
            phase=Phase.LOAD,
            xpath=invalid.path,
            value=str(invalid.value),
            stb_element=element,
        )


def _store_invalid_value(
    element: StBridgeElement,
    *,
    kind: _FieldKind,
    value: Any,
    xml_path: str,
    dict_path: str,
    reason: str,
    reporter: Reporter,
) -> None:
    element._ensure_extension._set_invalid_value(
        _InvalidValue(
            kind=kind,
            value=value,
            path=xml_path,
            reason=reason,
        )
    )
    reporter.error(
        message=f"{dict_path}: {reason}",
        code=Code.SCHEMA_ERROR,
        phase=Phase.LOAD,
        xpath=xml_path,
        value=str(value),
        stb_element=element,
    )
