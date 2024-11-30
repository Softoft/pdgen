import inspect
import logging
import typing
from collections.abc import Iterator, Sequence

from pdgen.factories.entities.method_signature import MethodSignature
from pdgen.factories.entities.type_info_collection import TypeInfoCollection
from pdgen.factories.entities.type_information import TypeInfo


class TypeHintService:
    def __init__(self):
        self._logger = logging.getLogger("pdgen")

    def get_type_infos(self, obj: object, excluded_names=None,
                       exclude_magic=True) -> TypeInfoCollection:
        excluded_names = excluded_names or []
        type_infos: list[TypeInfo] = list(self._exclude(self._get_type_information(obj), excluded=excluded_names))

        if exclude_magic:
            type_infos = list(self._exclude_magic(type_infos))

        if inspect.isfunction(obj) or inspect.ismethod(obj):
            return MethodSignature(type_infos)
        if inspect.isclass(obj):
            return TypeInfoCollection(type_infos)
        self._logger.warning(f"Unsupported object type: {type(obj)}")
        return TypeInfoCollection(type_infos)

    def _exclude(self, type_infos: Sequence[TypeInfo], *, excluded: Sequence[str]) -> Iterator[TypeInfo]:
        return filter(lambda t: t.name not in excluded, type_infos)

    def _exclude_magic(self, type_infos: Sequence[TypeInfo]) -> Iterator[TypeInfo]:
        return filter(lambda t: not t.is_magic(), type_infos)

    def _get_type_information(self, obj: object) -> list[TypeInfo]:
        return [TypeInfo(attr_name, attr_type) for attr_name, attr_type
                in typing.get_type_hints(obj).items()]
