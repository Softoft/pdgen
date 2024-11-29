from pdgen.factories.entities.type_information import TypeInfo


class TypeInfoCollection:
    def __init__(self, type_information_list: list[TypeInfo]):
        self.type_information_list: list[TypeInfo] = type_information_list
