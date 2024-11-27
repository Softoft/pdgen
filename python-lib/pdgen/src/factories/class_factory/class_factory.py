from src.factories.attribute_factory.attribute_factory import create_uml_attribute_factory, AttributeFactory
from src.factories.method_factory.method_factory import create_uml_method_factory, MethodFactory
from src.uml_types.types import UMLClass


class ClassFactory:
    def __init__(self, attribute_factory: AttributeFactory, method_factory: MethodFactory):
        self._attribute_factory: AttributeFactory = attribute_factory
        self._method_factory: MethodFactory = method_factory


    def create_uml_class(self, class_reference: type) -> UMLClass:
        print(f"UMLCLassFactory: Creating Class Reference: {class_reference}")
        class_name = class_reference.__name__
        attributes = self._attribute_factory.create_all(class_reference)
        methods = self._method_factory.create_all(class_reference)
        return UMLClass(class_name, attributes, methods)


def create_uml_class_factory() -> ClassFactory:
    attribute_factory = create_uml_attribute_factory()
    method_factory = create_uml_method_factory()
    return ClassFactory(attribute_factory, method_factory)