# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

import sys
import weakref
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass
from enum import Enum
from types import ModuleType
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    Final,
    Protocol,
    SupportsIndex,
    cast,
    get_args,
    get_origin,
)

from .._internal.name_converter import private_field_name, property_name
from ..stb_exceptions import NoneAccessError, SchemaError
from ._internal.stb_types import DataType
from ._internal.type_validation import any_to_typed_value as _any_to_typed_value
from ._internal.type_validation import make_attribute_setter as _make_attribute_setter
from ._internal.type_validation import str_to_typed_value as _str_to_typed_value

if TYPE_CHECKING:
    from ..stb_reporting import Phase, Reporter

_ATTR_NAME_XML_ELEMENT_NAME: Final[str] = "_xml_element_name"
_ATTR_NAME_FIELDS: Final[str] = "_fields"


class _FieldKind(Enum):
    ELEMENT = "element"
    ATTRIBUTE = "attribute"
    CONTENT = "content"


@dataclass(frozen=True, kw_only=True, slots=True)
class _FieldInfo:
    data_type: DataType | None = None
    py_type: type[Any] | str = str
    xml_name: str | None = None
    xml_type: str | None = None
    kind: _FieldKind = _FieldKind.ATTRIBUTE
    required: bool = False
    min_occurs: int | None = None
    max_occurs: int | None = None
    choices: tuple[str, ...] | None = None
    _py_type_str: str | None = None

    @property
    def py_type_str(self) -> str:
        if self._py_type_str is not None:
            return self._py_type_str
        result: str
        if isinstance(self.py_type, str):
            return self.py_type
        # py_typeがlistの場合は型引数を取得してlist[型名]の形式で返す
        origin = get_origin(self.py_type)
        if origin is list:
            args = getattr(self.py_type, "__args__", None)
            if args and len(args) == 1:
                arg_type = args[0]
                # 型引数が型の場合はその__name__を、文字列の場合はそのまま
                if isinstance(arg_type, type):
                    result = f"list[{arg_type.__name__}]"
                else:
                    result = f"list[{arg_type!s}]"
            else:
                result = "list"
        else:
            result = self.py_type.__name__
        object.__setattr__(self, "_py_type_str", result)
        return result


class _AutoModel(type):
    def __new__(
        cls: type[_AutoModel],
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, object],
    ) -> type:
        slots: set[str] = set()
        has_weakref = False
        for base in bases:
            if hasattr(base, "__slots__"):
                base_slots = base.__slots__
                if isinstance(base_slots, str):
                    slots.add(base_slots)
                elif isinstance(base_slots, (list, tuple)):
                    slots.update(base_slots)
                else:
                    raise AssertionError(f"{base.__name__}の__slots__が不正です")
        if "__weakref__" in slots:
            has_weakref = True
        own_slots = namespace.get("__slots__", ())
        if isinstance(own_slots, str):
            slots.add(own_slots)
        elif isinstance(own_slots, (list, tuple)):
            slots.update(own_slots)
        else:
            raise TypeError(f"{name}の__slots__が不正です")
        fields: dict[str, _FieldInfo] = cast(
            dict[str, _FieldInfo], namespace.get(_ATTR_NAME_FIELDS, {})
        )
        for key, field_info in fields.items():
            private_name: str = f"_{key}"
            slots.add(private_name)

            # getter
            def make_getter(
                p_name: str = private_name,
                f_name: str = key,
            ) -> Callable[[StBridgeElement], Any]:
                def getter(self: StBridgeElement) -> Any:
                    value: Any = getattr(self, p_name)
                    if value is None:
                        raise NoneAccessError(element=self, attr_name=f_name)
                    return value

                return getter

            # setter
            def make_setter(
                p_name: str = private_name,
                f_info: _FieldInfo = field_info,
                key_: str = key,
            ) -> Callable[[StBridgeElement, Any], None]:

                def setter_child(self: StBridgeElement, value: Any) -> None:
                    if isinstance(value, StBridgeElement):
                        value._attach_to_parent(self)
                    else:
                        raise TypeError(f"{key_}にはStBridgeElementを設定してください")
                    setattr(self, p_name, value)

                def setter_children(self: StBridgeElement, value: Any) -> None:
                    if not isinstance(value, Sequence) or isinstance(
                        value, (str, bytes)
                    ):
                        raise TypeError(
                            f"{key_}にはStBridgeElementのリストを設定してください"
                        )
                    if isinstance(value, _StBridgeElementList):
                        owner: StBridgeElement | None = value._parent
                        if owner is not None and owner is not self:
                            raise ValueError(
                                f"{key_}には他の要素の属性に設定されているリストは入れられません。"
                                "list()等でコピーしてから設定してください"
                            )
                    items: list[Any] = list(value)
                    for item in items:
                        if not isinstance(item, StBridgeElement):
                            raise TypeError(
                                f"{key_}はStBridgeElementのリストである必要があります"
                            )
                    current: Any = getattr(self, p_name, None)
                    if isinstance(current, _StBridgeElementList):
                        current.clear()
                        current.extend(items)
                    else:
                        setattr(
                            self,
                            p_name,
                            _StBridgeElementList(parent=self, iterable=items),
                        )

                if f_info.kind == _FieldKind.ELEMENT:
                    if f_info.max_occurs == 1:
                        return setter_child
                    else:
                        return setter_children
                else:
                    if f_info.data_type is None:
                        raise RuntimeError(
                            f"{name}.{key_}のdata_typeが指定されていません"
                        )
                    return _make_attribute_setter(
                        key=key_,
                        data_type=f_info.data_type,
                        has_choice=f_info.choices is not None,
                    )

            namespace[key] = property(make_getter(), make_setter())
            if field_info.kind == _FieldKind.ATTRIBUTE or (
                field_info.kind == _FieldKind.ELEMENT and field_info.max_occurs == 1
            ):

                def make_getter_or_none(
                    p_name: str = private_name,
                ) -> Callable[[StBridgeElement], Any | None]:
                    def getter(self: StBridgeElement) -> Any | None:
                        return getattr(self, p_name)

                    return getter

                namespace[f"{key}_or_none"] = property(
                    make_getter_or_none(), make_setter()
                )

        def __init__(self: Any, **kwargs: dict[str, Any]) -> None:
            StBridgeElement.__init__(self)
            for field_name, field_info in fields.items():
                value: Any = kwargs.get(field_name)
                if field_info.kind == _FieldKind.ELEMENT and field_info.max_occurs != 1:
                    if value is None:
                        value = _StBridgeElementList(parent=self)
                    elif isinstance(value, (list, tuple)):
                        value = _StBridgeElementList(parent=self, iterable=value)
                if isinstance(value, StBridgeElement):
                    value._attach_to_parent(self)
                setattr(self, f"_{field_name}", value)

        if "__init__" not in namespace:
            namespace["__init__"] = __init__
        if has_weakref and "__weakref__" in slots:
            slots.remove("__weakref__")
        namespace["__slots__"] = tuple(slots)
        return super().__new__(cls, name, bases, namespace)


@dataclass(slots=True, kw_only=True)
class _InvalidValue:
    kind: _FieldKind
    value: Any
    path: str
    reason: str


class _ExtensionData:
    __slots__ = (
        "__weakref__",
        "_attributes",
        "_children",
        "_invalid_values",
        "_parent_ref",
    )

    def __init__(self, *, parent: StBridgeElement) -> None:
        self._attributes: dict[str, Any] | None = None
        self._children: _StBridgeElementList[StBridgeElement] | None = None
        self._parent_ref: weakref.ref[StBridgeElement] | None = weakref.ref(parent)
        self._invalid_values: list[_InvalidValue] | None = None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, _ExtensionData):
            return False
        if self._attributes != other._attributes:
            return False
        return self._children == other._children

    def _set_attribute(self, name: str, value: Any) -> None:
        if self._attributes is None:
            self._attributes = {}
        self._attributes[name] = value

    def _get_attribute(self, name: str) -> Any:
        if self._attributes and name in self._attributes:
            return self._attributes[name]
        else:
            raise AttributeError(f"拡張属性{name}がありません")

    def _set_child(self, child: StBridgeElement) -> None:
        if self._children is None:
            self._children = _StBridgeElementList(
                parent=self._parent_ref() if self._parent_ref else None
            )
        self._children.append(child)
        child._attach_to_parent(self._parent_ref() if self._parent_ref else None)

    def _get_child(self, index: int) -> StBridgeElement:
        if self._children and 0 <= index < len(self._children):
            return self._children[index]
        else:
            raise IndexError(f"拡張子要素のインデックス{index}が範囲外です")

    def _get_children(self) -> list[StBridgeElement]:
        if self._children is None:
            self._children = _StBridgeElementList(
                parent=self._parent_ref() if self._parent_ref else None
            )
        return self._children

    def _set_invalid_value(self, invalid_value: _InvalidValue) -> None:
        if self._invalid_values is None:
            self._invalid_values = []
        self._invalid_values.append(invalid_value)


class StBridgeElement(metaclass=_AutoModel):
    """ST-Bridgeのすべての要素の基底クラス

    属性は`xxx`と`xxx_or_none`の2つのプロパティでアクセスできます。
    `xxx`はNoneのときNoneAccessErrorを投げます。
    Noneの時はNoneを返してほしい場合は`xxx_or_none`を使用します。
    """

    __slots__ = ("__weakref__", "_extension", "_parent_ref")
    _fields: ClassVar[dict[str, _FieldInfo]] = {}

    def __init__(self) -> None:
        self._parent_ref: weakref.ref[StBridgeElement] | None = None
        self._extension: _ExtensionData | None = None

    @property
    def ensure(self) -> _EnsureAccessorProtocol:
        """子要素がNoneの場合、生成してからアクセスできるアクセサ。

        element.ensure.xxx()の形で呼び出すと、子要素xxxがNoneの場合に
        インスタンスを新規作成し設定してから返します。
        Noneでない場合はそのまま返します。

        Returns:
            _EnsureAccessorProtocol: 子要素生成アクセサ。属性名と戻り値の型は、
            バージョンごとの型スタブが与えます。

        Examples:
            >>> members = stb.ensure.stb_model().ensure.stb_members()
        """
        return _EnsureAccessorBase(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, StBridgeElement):
            return False
        for key in self._fields:
            if getattr(self, f"_{key}") != getattr(other, f"_{key}"):
                return False
        return self._extension == other._extension

    def __repr__(self) -> str:
        field_strs = []
        for key in self._fields:
            value = getattr(self, f"_{key}")
            if value:
                field_strs.append(f"{key}={value}")
        field_str = ", ".join(field_strs)
        return f"{self.__class__.__name__}({field_str})"

    def _set_attribute_check(self, key: str, value: Any) -> tuple[str, DataType] | None:
        fi: _FieldInfo | None = self._fields.get(key)
        if fi is None:
            self._ensure_extension._set_attribute(key, value)
            return None
        if fi.kind == _FieldKind.ELEMENT:
            raise TypeError(
                f"{self._name_for_log(key)}は子要素なので属性を設定できません"
            )
        if fi.data_type is None:
            raise RuntimeError(
                f"{self.__class__.__name__}.{key}のdata_typeが指定されていません"
            )
        p_name: str = private_field_name(key)
        if value is None:
            setattr(self, p_name, None)
            return None
        if value == "":
            self._ensure_extension._set_invalid_value(
                _InvalidValue(
                    kind=_FieldKind.ATTRIBUTE,
                    value=value,
                    path=self._path_xml(attr_name=key),
                    reason="属性に空の値が指定されています",
                )
            )
            setattr(self, p_name, None)
            return None
        return key, fi.data_type

    def _set_attribute_by_any(self, key: str, value: Any) -> None:
        fi: _FieldInfo | None = self._fields.get(key)
        if fi is None:
            self._ensure_extension._set_attribute(key, value)
            return
        if fi.kind == _FieldKind.ELEMENT:
            raise TypeError(
                f"{self._name_for_log(key)}は子要素なので属性を設定できません"
            )
        if fi.data_type is None:
            raise RuntimeError(
                f"{self.__class__.__name__}.{key}のdata_typeが指定されていません"
            )
        p_name: str = private_field_name(key)
        if value is None:
            setattr(self, p_name, None)
            return
        if value == "":
            self._ensure_extension._set_invalid_value(
                _InvalidValue(
                    kind=_FieldKind.ATTRIBUTE,
                    value=value,
                    path=self._path_xml(attr_name=key),
                    reason="属性に空の値が指定されています",
                )
            )
            setattr(self, p_name, None)
            return
        try:
            typed_value: Any = _any_to_typed_value(
                value, fi.data_type, element=self, attr_name=key
            )
            setattr(self, p_name, typed_value)
        except SchemaError as e:
            self._ensure_extension._set_invalid_value(
                _InvalidValue(
                    kind=_FieldKind.ATTRIBUTE,
                    value=value,
                    path=self._path_xml(attr_name=key),
                    reason=str(e),
                )
            )
            setattr(self, p_name, None)

    def _set_attribute_by_str(
        self, key: str, value: str | None, raw_attr_name: str
    ) -> None:
        fi: _FieldInfo | None = self._fields.get(key)
        if fi is None:
            self._ensure_extension._set_attribute(raw_attr_name, value)
            return
        if fi.kind == _FieldKind.ELEMENT:
            raise TypeError(
                f"{self._name_for_log(key)}は子要素なので属性を設定できません"
            )
        if fi.data_type is None:
            raise RuntimeError(
                f"{self.__class__.__name__}.{key}のdata_typeが指定されていません"
            )
        p_name: str = private_field_name(key)
        if value is None:
            setattr(self, p_name, None)
            return
        if value == "":
            self._ensure_extension._set_invalid_value(
                _InvalidValue(
                    kind=_FieldKind.ATTRIBUTE,
                    value=value,
                    path=self._path_xml(attr_name=key),
                    reason="属性に空の値が指定されています",
                )
            )
            setattr(self, p_name, None)
            return
        try:
            typed_value: Any = _str_to_typed_value(
                value, fi.data_type, element=self, attr_name=key
            )
            setattr(self, p_name, typed_value)
        except SchemaError as e:
            self._ensure_extension._set_invalid_value(
                _InvalidValue(
                    kind=_FieldKind.ATTRIBUTE,
                    value=value,
                    path=self._path_xml(attr_name=key),
                    reason=str(e),
                )
            )
            setattr(self, p_name, None)

    def _field_info(self, attr_name: str) -> _FieldInfo:
        try:
            return self._fields[attr_name]
        except KeyError:
            raise RuntimeError(
                f"{self.__class__.__name__}に属性{attr_name}はありません"
            ) from None

    @classmethod
    def _xml_class_name(cls) -> str:
        if hasattr(cls, _ATTR_NAME_XML_ELEMENT_NAME):
            return str(getattr(cls, _ATTR_NAME_XML_ELEMENT_NAME))
        return cls.__name__

    @classmethod
    def _child_class(cls, attr_name: str) -> type[StBridgeElement]:
        """子要素の型を返します。

        リストの子要素の場合はリストアイテムの型を返します。
        """
        field_info: _FieldInfo | None = cls._fields.get(attr_name)
        if field_info is None:
            raise ValueError(f"{cls.__name__}に属性{attr_name}はありません")
        if field_info.kind is not _FieldKind.ELEMENT:
            raise ValueError(f"{cls.__name__}.{attr_name}は子要素ではありません")
        py_type: type[Any] | str = field_info.py_type
        if get_origin(py_type) is list:
            args: tuple[Any, ...] = get_args(py_type)
            if len(args) != 1:
                raise RuntimeError(
                    f"{cls.__name__}.{attr_name}のリスト型情報が不正です"
                )
            py_type = args[0]
        if isinstance(py_type, str):
            # 文字列で保持されるものは、定義モジュールから解決する
            class_name: str = py_type.removeprefix("list[").removesuffix("]")
            module: ModuleType | None = sys.modules.get(cls.__module__)
            if module is None:
                raise ValueError(f"{cls.__module__}が読み込まれていません")
            try:
                py_type = getattr(module, class_name)
            except AttributeError:
                raise ValueError(
                    f"{cls.__module__}に{class_name}はありません"
                ) from None
        if not isinstance(py_type, type) or not issubclass(py_type, StBridgeElement):
            raise TypeError(f"{cls.__name__}.{attr_name}の子要素型情報が不正です")
        return py_type

    def _xml_name(self, attr_name: str | None = None) -> str:
        """XML上の名前

        attr_nameを省略した場合はこの要素のXML要素名を返す。
        attr_nameを指定した場合は、その属性のXML属性名を返す。
        attr_nameが子要素の場合は、その子要素のXML要素名を返す。
        """
        if attr_name:
            field_info: _FieldInfo = self._field_info(attr_name)
            if field_info.kind is _FieldKind.ELEMENT:
                return self._child_class(attr_name)._xml_class_name()
            return field_info.xml_name or attr_name
        else:
            return self._xml_class_name()

    def _is_attr(self, attr_name: str) -> bool:
        return self._field_info(attr_name).kind == _FieldKind.ATTRIBUTE

    def _is_child(self, attr_name: str) -> bool:
        return self._field_info(attr_name).kind == _FieldKind.ELEMENT

    def _is_children(self, attr_name: str) -> bool:
        fi: _FieldInfo = self._field_info(attr_name)
        return fi.kind == _FieldKind.ELEMENT and fi.max_occurs != 1

    def _is_content(self, attr_name: str) -> bool:
        return self._field_info(attr_name).kind == _FieldKind.CONTENT

    def _name_for_log(self, attr_name: str | None = None) -> str:
        result: str = self.__class__.__name__
        args: list[str] = []
        pickup_attrs: tuple[str, ...] = ("id", "name", "pos", "guid")
        for attr in pickup_attrs:
            p_name: str = private_field_name(attr)
            if hasattr(self, p_name):
                value: Any = getattr(self, p_name)
                if value:
                    args.append(f"{attr}={value}")
        if args:
            result += f"({', '.join(args)})"
        if attr_name:
            result += f".{attr_name}"
        return result

    @property
    def _parent(self) -> StBridgeElement | None:
        return self._parent_ref() if self._parent_ref else None

    def _attach_to_parent(self, parent: StBridgeElement | None) -> None:
        if parent is None:
            self._parent_ref = None
        else:
            self._parent_ref = weakref.ref(parent)

    def _path_py(self, attr_name: str | None = None) -> str:
        parts: list[str] = []
        if attr_name:
            parts.append(property_name(attr_name))
        current: StBridgeElement | None = self
        while current is not None:
            parent: StBridgeElement | None = current._parent
            if parent is not None:
                for key, field in parent._fields.items():
                    value = getattr(parent, private_field_name(key))
                    if field.kind == _FieldKind.ELEMENT:
                        if field.max_occurs == 1:
                            if value is current:
                                parts.append(property_name(key))
                                break
                        else:
                            if isinstance(value, list):
                                for idx, item in enumerate(value):
                                    if item is current:
                                        parts.append(f"{property_name(key)}[{idx}]")
                                        break
                                else:
                                    continue
                                break
            else:
                parts.append(current.__class__.__name__)
            current = parent
        parts.reverse()
        return ".".join(parts)

    def _path_xml(self, attr_name: str | None = None) -> str:
        """この要素のXPath。

        attr_nameを指定した場合はその属性までのXPath。
        """
        parts: list[str] = []
        if attr_name:
            field_info: _FieldInfo = self._field_info(attr_name)
            match field_info.kind:
                case _FieldKind.ELEMENT:
                    parts.append(self._xml_name(attr_name))
                case _FieldKind.CONTENT:
                    parts.append("text()")
                case _FieldKind.ATTRIBUTE:
                    parts.append(f"@{self._xml_name(attr_name)}")
        current: StBridgeElement | None = self
        while current is not None:
            parent: StBridgeElement | None = current._parent
            if parent is None:
                parts.append(current._xml_name())
                parts.append("")
                current = parent
                continue
            step: str | None = None
            for key, field in parent._fields.items():
                if field.kind != _FieldKind.ELEMENT:
                    continue
                value = getattr(parent, private_field_name(key))
                if field.max_occurs == 1:
                    if value is current:
                        step = current._xml_name()
                        break
                elif isinstance(value, list):
                    for idx, item in enumerate(value):
                        if item is current:
                            step = f"{current._xml_name()}[{idx + 1}]"
                            break
                    if step is not None:
                        break
            if step is None:
                # 拡張子要素は_fieldsに無いため、拡張側から位置を探す。
                step = parent._extension_xpath_step(current)
            if step is not None:
                parts.append(step)
            current = parent
        parts.reverse()
        return "/".join(parts)

    def _extension_xpath_step(self, child: StBridgeElement) -> str | None:
        ext: _ExtensionData | None = self._extension
        children = ext._children if ext is not None else None
        if not children:
            return None
        name: str = child._xml_name()
        index: int = 0
        for item in children:
            if item._xml_name() != name:
                continue
            index += 1
            if item is child:
                return f"{name}[{index}]"
        return None

    def _get_ext_attr(self, attr_name: str) -> Any:
        if self._extension:
            return self._extension._get_attribute(attr_name)
        else:
            raise AttributeError(f"{self._path_py(attr_name)}がありません")

    def _get_ext_children(self) -> list[StBridgeElement]:
        if self._extension is None:
            self._extension = _ExtensionData(parent=self)
        return self._extension._get_children()

    def _get_ext_child(self, index: int) -> StBridgeElement:
        if self._extension is None:
            self._extension = _ExtensionData(parent=self)
        return self._extension._get_children()[index]

    def _set_parent_all(self) -> None:
        for key, field in self._fields.items():
            value = getattr(self, private_field_name(key))
            if field.kind == _FieldKind.ELEMENT:
                if field.max_occurs == 1:
                    if isinstance(value, StBridgeElement):
                        value._attach_to_parent(self)
                        value._set_parent_all()
                else:
                    if isinstance(value, list):
                        for item in value:
                            if isinstance(item, StBridgeElement):
                                item._attach_to_parent(self)
                                item._set_parent_all()
        if self._extension is not None and self._extension._children:
            for child in self._extension._children:
                child._attach_to_parent(self)
                child._set_parent_all()

    @classmethod
    def _get_module(cls) -> ModuleType:
        """このクラスが定義されているモジュール"""
        module: ModuleType | None = sys.modules.get(cls.__module__)
        if module is None:
            raise ValueError(f"{cls.__module__}が読み込まれていません")
        return module

    @classmethod
    def _try_get_module_version(cls) -> str | None:
        """このクラスが定義されているモジュールのST-Bridgeバージョン。

        VERSIONが未定義の場合はNoneを返す。
        VERSIONが定義済みで型や値が不正な場合はValueErrorを投げる。
        """
        module: ModuleType = cls._get_module()
        version: object = getattr(module, "VERSION", None)
        if version is None:
            return None
        if not isinstance(version, str) or not version:
            raise ValueError(f"{cls.__module__}のVERSION定数には空でないstrが必要です")
        return version

    @classmethod
    def _create_instance(cls, class_name: str) -> StBridgeElement:
        """同じモジュールのclass_nameで指定されたクラスのインスタンス"""
        try:
            module: ModuleType = sys.modules[cls.__module__]
            new_class: type[StBridgeElement] = getattr(module, class_name)
            return new_class()
        except AttributeError:
            raise ValueError(f"{cls.__module__}に{class_name}はありません") from None

    @classmethod
    def _create_child_instance(cls, attr_name: str) -> StBridgeElement:
        if attr_name in cls._fields:
            field_info: _FieldInfo = cls._fields[attr_name]
        else:
            raise ValueError(f"{cls.__name__}に属性{attr_name}はありません")
        if field_info.kind is not _FieldKind.ELEMENT:
            raise ValueError(f"{cls.__name__}.{attr_name}は子要素ではありません")
        return cls._create_instance(field_info.py_type_str)

    def _ensure_child(self, attr_name: str) -> StBridgeElement:
        p_name: str = private_field_name(attr_name)
        if hasattr(self, p_name):
            value: Any = getattr(self, p_name)
            if isinstance(value, StBridgeElement):
                return value
        instance: StBridgeElement = self._create_child_instance(attr_name)
        setattr(self, attr_name, instance)
        return instance

    @property
    def _ensure_extension(self) -> _ExtensionData:
        if self._extension is None:
            self._extension = _ExtensionData(parent=self)
        return self._extension


class StBridgeRoot(StBridgeElement):
    """ST-Bridgeのルート要素ST_BRIDGEの基底クラス。

    バージョンごとのStBridgeクラスがこのクラスを継承する。
    load,dump等のバージョンを問わず利用する関数の型ヒントではこのクラスを用いる。
    """

    __slots__ = ()

    @property
    def version(self) -> str:
        """ST-Bridgeのバージョン。

        Returns:
            str: "2.1.0"のようなバージョン文字列。

        Raises:
            NotImplementedError: サブクラスではなく、この基底クラスのまま参照した場合。
        """
        raise NotImplementedError("versionプロパティはサブクラスで実装されます")

    def _set_version(
        self, *, reporter: Reporter | None = None, phase: Phase | None = None
    ) -> None:
        from ..stb_reporting import Code

        version: str | None = self._try_get_module_version()
        if version is not None:
            p_field_name: str = private_field_name("version")
            if hasattr(self, p_field_name):
                setattr(self, p_field_name, version)
        elif reporter is not None:
            reporter.error(
                message=f"{self.__class__.__name__}の定義モジュールにVERSIONが定義されていません",
                code=Code.DEVELOPER_ERROR,
                phase=phase,
                stb_element=self,
                attr_name="version",
            )


class _StBridgeElementList[TElement: StBridgeElement](list[TElement]):
    """子要素を格納するリスト

    ユーザーには普通のlistとして見せるが、parent処理を行うために内部的にはこのクラスで管理する。"""

    __slots__ = ("__weakref__", "_parent_ref")

    def __init__(
        self,
        parent: StBridgeElement | None = None,
        iterable: Iterable[TElement] = (),
    ) -> None:
        super().__init__()
        self._parent_ref: weakref.ref[StBridgeElement] | None = None
        if parent is not None:
            self._attach_to_parent(parent)
        if iterable:
            self.extend(iterable)

    def append(self, item: TElement) -> None:
        if isinstance(item, StBridgeElement):
            if self._parent is not None:
                item._attach_to_parent(self._parent)
        else:
            raise TypeError("StBridgeElementListにはStBridgeElementのみ追加できます")
        super().append(item)

    def extend(self, it: Iterable[TElement]) -> None:
        for x in it:
            if isinstance(x, StBridgeElement):
                if self._parent is not None:
                    x._attach_to_parent(self._parent)
            else:
                raise TypeError(
                    "StBridgeElementListにはStBridgeElementのみ追加できます"
                )
            super().append(x)

    def insert(self, i: SupportsIndex, item: TElement) -> None:
        if isinstance(item, StBridgeElement):
            if self._parent is not None:
                item._attach_to_parent(self._parent)
        else:
            raise TypeError("StBridgeElementListにはStBridgeElementのみ追加できます")
        super().insert(i, item)

    def remove(self, value: TElement) -> None:
        super().remove(value)
        if (
            isinstance(value, StBridgeElement)
            and self._parent is not None
            and not any(x is value for x in self)
        ):
            value._attach_to_parent(None)

    def clear(self) -> None:
        for item in self:
            if isinstance(item, StBridgeElement) and self._parent is not None:
                item._attach_to_parent(None)
        super().clear()

    def __delitem__(self, key: SupportsIndex | slice[Any, Any, Any]) -> None:
        old_item: TElement | None
        if isinstance(key, slice):
            old_items: list[TElement] = self[key]
            super().__delitem__(key)
            for old_item in old_items:
                if (
                    isinstance(old_item, StBridgeElement)
                    and self._parent is not None
                    and not any(x is old_item for x in self)
                ):
                    old_item._attach_to_parent(None)
            return
        old_item = self[key] if int(key) < len(self) else None
        super().__delitem__(key)
        if (
            isinstance(old_item, StBridgeElement)
            and self._parent is not None
            and not any(x is old_item for x in self)
        ):
            old_item._attach_to_parent(None)

    def pop(self, index: SupportsIndex = -1) -> TElement:
        item = super().pop(index)
        if (
            isinstance(item, StBridgeElement)
            and self._parent is not None
            and not any(x is item for x in self)
        ):
            item._attach_to_parent(None)
        return item

    def __setitem__(
        self,
        i: SupportsIndex | slice[Any, Any, Any],
        item: TElement | Iterable[TElement],
    ) -> None:
        if isinstance(i, slice):
            raise NotImplementedError("スライスの代入はサポートしていません")
        if not isinstance(item, StBridgeElement):
            raise TypeError("子要素リストにはStBridgeElementのみ追加できます")
        old_item: TElement = self[i]
        if old_item is item:
            return
        if self._parent is not None:
            item._attach_to_parent(self._parent)
        super().__setitem__(i, item)
        if self._parent is not None and not any(x is old_item for x in self):
            old_item._attach_to_parent(None)

    @property
    def _parent(self) -> StBridgeElement | None:
        return self._parent_ref() if self._parent_ref else None

    def _attach_to_parent(self, parent: StBridgeElement) -> None:
        self._parent_ref = weakref.ref(parent)
        for item in self:
            item._attach_to_parent(parent)


class _StBridgeExtensionElement(StBridgeElement):
    __slots__ = ("_extension_attrs", "_name")

    def __init__(self, name: str, attributes: dict[str, Any] | None = None) -> None:
        super().__init__()
        if attributes:
            self._extension_attrs = attributes
        self._name: str = name

    def _xml_name(self, attr_name: str | None = None) -> str:
        if attr_name is None:
            return self._name
        else:
            return attr_name


class _EnsureAccessorProtocol(Protocol):
    pass


class _EnsureAccessorBase(_EnsureAccessorProtocol):
    """
    ensureプロパティが返す子要素生成アクセサ。

    実行時の実装はこのクラスのみで行い、要素の型ごとの属性名と戻り値の型は
    stb_v2_1_0.pyiなどのスタブが_EnsureAccessorProtocolを継承して与える。
    """

    __slots__ = ("_owner",)

    def __init__(self, owner: StBridgeElement) -> None:
        self._owner = owner

    # not TYPE_CHECKINGにより__getattr__を型チェッカから隠す。
    # 見えているとスタブで定義していない属性で方エラーが出ず、
    # 属性名のtypoの危険性がある。
    if not TYPE_CHECKING:

        def __getattr__(self, name: str) -> Any:
            if name in self._owner._fields:
                field_info: _FieldInfo = self._owner._field_info(name)
                if field_info.kind == _FieldKind.ELEMENT:
                    return lambda: self._owner._ensure_child(name)
                else:
                    raise AttributeError(
                        f"{self._owner.__class__.__name__}.{name}は子要素ではありません"
                    )
