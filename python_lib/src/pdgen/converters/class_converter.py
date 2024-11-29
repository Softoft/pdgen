from pdgen.converters.attribute_converter import AttributeConverter
from pdgen.converters.method_converter import MethodConverter
from pdgen.uml_types.types import UMLClass


class ClassConverter:
    def __init__(self, attribute_converter, method_converter):
        self.attribute_converter: AttributeConverter = attribute_converter
        self.method_converter: MethodConverter = method_converter

    def convert(self, uml_class: UMLClass) -> list[str]:
        """
        Converts a UMLClass to PlantUML format.

        Args:
            uml_class (UMLClass): The class to convert.

        Returns:
            list[str]: PlantUML lines representation of the class.
        """
        if not uml_class.name:
            raise ValueError("UMLClass Name cant be empty!")

        lines = [f"class {uml_class.name} {{"]

        for attribute in uml_class.attributes:
            lines.append(self.attribute_converter.convert(attribute))

        for method in uml_class.methods:
            lines.append(self.method_converter.convert(method))
        lines.append("}")
        return lines
