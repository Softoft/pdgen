import logging

from pdgen.factories.class_factory.class_factory import ClassFactory
from pdgen.repositories.class_repository import ClassRepository
from pdgen.uml_types.types import UMLDiagram


class DiagramFactory:
    def __init__(self, uml_class_factory: ClassFactory, class_repository: ClassRepository):
        self._class_factory: ClassFactory = uml_class_factory
        self._class_repository: ClassRepository = class_repository
        self._loger = logging.getLogger("pdgen")

    def create_diagram(self) -> UMLDiagram:
        classes = self._class_repository.get_all()
        comma_separated_classes = ", ".join([cls.__name__ for cls in classes])
        self._loger.info("Creating Diagram for classes %s", comma_separated_classes)
        uml_classes = [self._class_factory.create_uml_class(cls) for cls in classes]
        return UMLDiagram(frozenset(uml_classes))
