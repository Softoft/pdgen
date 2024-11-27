from src.uml_types.types import UMLAttribute


class PlantUMLAttributeConverter:
    def convert(self, attribute: UMLAttribute) -> str:
        """
        Converts a UMLAttribute to PlantUML format.

        Args:
            attribute (UMLAttribute): The attribute to convert.

        Returns:
            str: PlantUML representation of the attribute.
        """
        return f"    {attribute.name} : {attribute.attr_type}"
