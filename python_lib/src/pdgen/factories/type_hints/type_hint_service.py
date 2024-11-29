import inspect
import typing

from pdgen.factories.entities.method_signature import MethodSignature
from pdgen.factories.entities.type_info_collection import TypeInfoCollection
from pdgen.factories.entities.type_information import TypeInfo


class TypeHintService:
    def get_type_infos(self, obj: object, excluded=None,
                       allow_dunderscore=False) -> TypeInfoCollection:
        excluded = excluded or []
        type_infos = list(filter(lambda t: t.name not in excluded, self._get_type_information(obj)))

        if not allow_dunderscore:
            type_infos = list(filter(lambda t: not self._is_dunderscore(t.name), type_infos))

        if inspect.isfunction(obj):
            return MethodSignature(type_infos)
        return TypeInfoCollection(type_infos)

    def _is_dunderscore(self, member_name: str) -> bool:
        return member_name.startswith('__') and member_name.endswith('__')

    def _has_return_type(self, type_information_list: list[TypeInfo]) -> bool:
        return any(map(lambda t: t.name == 'return', type_information_list))

    def _get_type_information(self, obj: object) -> list[TypeInfo]:
        return [TypeInfo(attr_name, attr_type) for attr_name, attr_type
                in typing.get_type_hints(obj).items()]
