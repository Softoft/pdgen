from src.services.uml_attribute_factory import create_uml_attribute_factory, UMLAttributeFactory
from src.services.uml_method_factory import create_uml_method_factory, UMLMethodFactory
from src.uml_types.types import UMLClass


class UMLClassFactory:
    def __init__(self, attribute_factory, method_factory):
        self._attribute_factory: UMLAttributeFactory = attribute_factory
        self._method_factory: UMLMethodFactory = method_factory


    def create_uml_class(self, class_reference: type) -> UMLClass:
        print(f"UMLCLassFactory: Creating Class Reference: {class_reference}")
        class_name = class_reference.__name__
        attributes = self._attribute_factory.create_all(class_reference)
        methods = self._method_factory.create_all(class_reference)
        return UMLClass(class_name, attributes, methods)


def create_uml_class_factory() -> UMLClassFactory:
    attribute_factory = create_uml_attribute_factory()
    method_factory = create_uml_method_factory()
    return UMLClassFactory(attribute_factory, method_factory)