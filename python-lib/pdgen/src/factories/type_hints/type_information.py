import dataclasses


@dataclasses.dataclass(frozen=True)
class TypeInformation:
    name: str
    type: type


class TypeInfoCollection:
    def __init__(self, type_information_list: list[TypeInformation]):
        self.type_information_list: list[TypeInformation] = type_information_list


@dataclasses.dataclass
class MethodSignature(TypeInfoCollection):
    return_type: type | None

    def __init__(self, type_information_list: list[TypeInformation]):
        possible_return_type = list(filter(lambda x: x.name=="return", type_information_list))
        assert len(possible_return_type) < 2, "MethodSignature must have none or one return type"
        if len(possible_return_type) == 0:
            self.return_type = None
        else:
            self.return_type = possible_return_type[0].type
        parameters = list(filter(lambda x: x.name!="return", type_information_list))
        super().__init__(parameters)


    def has_return_type(self) -> bool:
        return self.return_type is not None