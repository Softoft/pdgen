from src.uml_types.types import UMLDiagram


class DiagramFactory:
    def __init__(self, uml_class_factory, class_repository):
        self._uml_class_factory = uml_class_factory
        self._class_repository = class_repository

    def create_diagram(self) -> UMLDiagram:
        classes = self._class_repository.get_all()
        uml_classes = [self._uml_class_factory.create_uml_class(cls) for cls in classes]
        return UMLDiagram(uml_classes)
