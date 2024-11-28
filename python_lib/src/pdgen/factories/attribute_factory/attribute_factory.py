from pdgen.factories.type_hints.type_hint_service import TypeHintService
from pdgen.factories.type_hints.type_information import TypeInfoCollection, TypeInformation
from pdgen.uml_types.types import UMLAttribute

class AttributeFactory:
    def __init__(self, type_hint_service: TypeHintService):
        self._type_hint_service: TypeHintService = type_hint_service

    def create_all(self, cls: type) -> list[UMLAttribute]:
        """
        Create all UML _attributes for a given class. This method_factory will return a list of UMLAttribute
        Class Attributes have priority over __init__ _attributes. If an attribute_factory is present in both
        class and __init__ _attributes, it will only be returned once.
        Args:
            cls:

        Returns:

        """
        class_attrs: TypeInfoCollection = self._type_hint_service.get_type_information(cls)
        init_attrs: TypeInfoCollection = (self._type_hint_service.
                                          get_type_information(cls.__init__, ['self']))

        class_attr_names: frozenset[str] = frozenset(
            {attr.name for attr in class_attrs.type_information_list}
        )

        ordered_attrs: list[TypeInformation] = class_attrs.type_information_list + [
            attr for attr in init_attrs.type_information_list if attr.name not in class_attr_names
        ]

        return [UMLAttribute(attr.name, attr.type.__name__, attr.visibility)
                for attr in ordered_attrs]
