from src.services.type_hints.type_hint_service import TypeHintService
from src.services.type_hints.type_information import TypeInfoCollection, TypeInformation
from src.uml_types.types import UMLAttribute

class UMLAttributeFactory:
    def __init__(self, type_hint_service):
        self._type_hint_service: TypeHintService = type_hint_service

    def create_all(self, cls: type) -> list[UMLAttribute]:
        class_attrs: TypeInfoCollection = (self._type_hint_service
                                           .get_type_information(cls))
        init_attrs: TypeInfoCollection = (self._type_hint_service
                                          .get_type_information(cls.__init__, ['self']))
        union_attrs: list[TypeInformation] = list(set(class_attrs.type_information_list) |
                                                  set(init_attrs.type_information_list))
        return [UMLAttribute(attr.name, attr.type.__name__) for attr in union_attrs]

