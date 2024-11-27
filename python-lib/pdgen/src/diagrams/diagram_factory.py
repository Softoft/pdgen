from src.services.class_repository import ClassRepository
from src.services.uml_class_factory import create_uml_class_factory, UMLClassFactory
from src.uml_types.types import UMLDiagram


class DiagramFactory:
    def __init__(self, uml_class_factory, class_repository):
        self._uml_class_factory: UMLClassFactory = uml_class_factory
        self._class_repository: ClassRepository = class_repository

    def create_diagram(self) -> UMLDiagram:
        classes = self._class_repository.get_all()
        print("Diagram Factory: " + ",".join(classes))
        uml_classes = [self._uml_class_factory.create_uml_class(cls) for cls in classes]
        return UMLDiagram(frozenset(uml_classes))


def create_diagram_factory() -> DiagramFactory:
    uml_class_factory = create_uml_class_factory()
    class_repository = ClassRepository()
    return DiagramFactory(uml_class_factory, class_repository)