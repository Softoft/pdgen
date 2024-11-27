from src.uml_types.types import UMLAttribute


class AttributeConverter:
    def convert(self, attribute: UMLAttribute) -> str:
        """
        Converts a UMLAttribute to PlantUML format.

        Args:
            attribute (UMLAttribute): The attribute_factory to convert.

        Returns:
            str: PlantUML representation of the attribute_factory.
        """
        return f"    {attribute.name} : {attribute.attr_type}"
