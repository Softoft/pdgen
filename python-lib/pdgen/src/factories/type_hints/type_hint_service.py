import inspect
import typing
from types import FunctionType

from src.factories.type_hints.type_information import MethodSignature, TypeInformation, \
    TypeInfoCollection


class TypeHintService:
    def get_type_information(self, obj: object, excluded=None,
                             allow_dunderscore=False) -> TypeInfoCollection:
        if excluded is None:
            excluded = []
        included = list(filter(lambda t: t.name not in excluded, self._get_type_information(obj)))

        if not allow_dunderscore:
            included = list(filter(lambda t: not self._is_dunderscore(t.name), included))

        if inspect.isfunction(obj):
            return MethodSignature(included)
        return TypeInfoCollection(included)

    def _is_dunderscore(self, member_name: str) -> bool:
        return member_name.startswith('__') and member_name.endswith('__')

    def _has_return_type(self, type_information_list: list[TypeInformation]) -> bool:
        return any(map(lambda t: t.name == 'return', type_information_list))

    def _get_type_information(self, obj: object) -> list[TypeInformation]:
        return [TypeInformation(attr_name, attr_type) for attr_name, attr_type
                in typing.get_type_hints(obj).items()]
