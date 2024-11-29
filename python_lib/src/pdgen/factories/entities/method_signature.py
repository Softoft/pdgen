import dataclasses
from types import NoneType

from pdgen.factories.entities.type_info_collection import TypeInfoCollection
from pdgen.factories.entities.type_information import TypeInfo


def _separate_return_type(type_infos: list[TypeInfo]) -> tuple[list[TypeInfo], type | None]:
    return_type = None
    parameters = []
    for type_info in type_infos:
        if type_info.name == "return":
            return_type = type_info.type
        else:
            parameters.append(type_info)
    return parameters, return_type


@dataclasses.dataclass
class MethodSignature(TypeInfoCollection):
    return_type: type | None | NoneType

    def __init__(self, type_information_list: list[TypeInfo]):
        params, possible_return_type = _separate_return_type(type_information_list)
        self.return_type = possible_return_type
        super().__init__(params)

    def get_return_type_as_str(self) -> str:
        if self.return_type is None:
            return ""
        if self.return_type == NoneType:
            return "None"
        return self.return_type.__name__

    def has_return_type(self) -> bool:
        return self.return_type is not None
