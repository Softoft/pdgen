from src.services.uml_attribute_factory import UMLAttributeFactory
from src.services.uml_method_factory import UMLMethodFactory
from src.uml_types.types import UMLClass


class UMLClassFactory:
    def __init__(self, attribute_factory, method_factory):
        self._attribute_factory: UMLAttributeFactory = attribute_factory
        self._method_factory: UMLMethodFactory = method_factory


    def create_uml_class(self, class_reference):
        class_name = class_reference.__name__
        attributes = self._attribute_factory.create_all(class_reference)
        methods = self._method_factory.create_all(class_reference)
        return UMLClass(class_name, attributes, methods)