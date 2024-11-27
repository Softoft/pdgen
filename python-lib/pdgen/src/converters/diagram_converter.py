from src.converters.class_converter import ClassConverter
from src.uml_types.types import UMLDiagram


class DiagramConverter:
    def __init__(self, class_converter):
        self._class_converter: ClassConverter = class_converter

    def convert(self, uml_diagram: UMLDiagram) -> str:
        plantuml_lines = ["@startuml", "skinparam dpi 600"]

        for uml_class in uml_diagram.classes:
            class_lines = self._class_converter.convert(uml_class)
            plantuml_lines.extend([""] + class_lines + [""])

        plantuml_lines.append("@enduml")

        return "\n".join(plantuml_lines)
