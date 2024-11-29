import logging

from pdgen.factories.attribute_factory.attribute_factory import AttributeFactory
from pdgen.factories.method_factory.method_factory import MethodFactory
from pdgen.uml_types.types import UMLClass


class ClassFactory:
    def __init__(self, attribute_factory: AttributeFactory, method_factory: MethodFactory):
        self._attribute_factory: AttributeFactory = attribute_factory
        self._method_factory: MethodFactory = method_factory
        self._logger = logging.getLogger("pdgen")

    def create_uml_class(self, class_reference: type) -> UMLClass:
        self._logger.info("UMLCLassFactory: Creating Class Reference: %s",
                          class_reference)
        class_name = class_reference.__name__
        attributes = self._attribute_factory.create_all(class_reference)
        methods = self._method_factory.create_all(class_reference)
        return UMLClass(class_name, attributes, methods)
