from src.factories.class_factory.class_factory import ClassFactory
from src.repositories.class_repository import ClassRepository
from src.uml_types.types import UMLDiagram


class DiagramFactory:
    def __init__(self, uml_class_factory: ClassFactory, class_repository: ClassRepository):
        self._class_factory: ClassFactory = uml_class_factory
        self._class_repository: ClassRepository = class_repository

    def create_diagram(self) -> UMLDiagram:
        classes = self._class_repository.get_all()
        print("Diagram Factory: " + ",".join(classes))
        uml_classes = [self._class_factory.create_uml_class(cls) for cls in classes]
        return UMLDiagram(frozenset(uml_classes))
