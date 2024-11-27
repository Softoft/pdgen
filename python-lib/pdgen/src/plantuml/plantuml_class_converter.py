from src.plantuml.plantuml_attribute_converter import PlantUMLAttributeConverter
from src.plantuml.plantuml_method_converter import PlantUMLMethodConverter
from src.uml_types.types import UMLClass


class PlantUMLClassConverter:
    def __init__(self):
        self.attribute_converter = PlantUMLAttributeConverter()
        self.method_converter = PlantUMLMethodConverter()

    def convert(self, uml_class: UMLClass) -> list[str]:
        """
        Converts a UMLClass to PlantUML format.

        Args:
            uml_class (UMLClass): The class to convert.

        Returns:
            str: PlantUML representation of the class.
        """
        lines = [f"class {uml_class.name} {{"]

        for attribute in uml_class.attributes:
            lines.append(self.attribute_converter.convert(attribute))

        for method in uml_class.methods:
            lines.append(self.method_converter.convert(method))
        lines.append("}")
        return lines