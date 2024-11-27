import plantuml

from src.plantuml.plantuml_class_converter import PlantUMLClassConverter
from src.uml_types.types import UMLDiagram


class PlantUMLConverter:

    def convert(self, uml_diagram: UMLDiagram) -> str:
        puml_class_converter = PlantUMLClassConverter()
        plantuml_lines = ["@startuml", "skinparam dpi 600"]

        for uml_class in uml_diagram.classes:
            class_lines = puml_class_converter.convert(uml_class)
            plantuml_lines.extend([""] + class_lines + [""])

        plantuml_lines.append("@enduml")

        return "\n".join(plantuml_lines)

