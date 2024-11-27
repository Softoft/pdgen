from src.uml_types.types import UMLAttribute


class AttributeConverter:
    def convert(self, attribute: UMLAttribute) -> str:
        """
        Converts a UMLAttribute to PlantUML format.

        Args:
            attribute (UMLAttribute): The attribute_factory to convert.

        Returns:
            str: PlantUML representation of the attribute_factory.

        Raises:
            ValueError: If the attribute's name or type is empty.
        """
        if not attribute.name:
            raise ValueError("UML Attribute name cannot be empty!")
        if not attribute.attr_type:
            raise ValueError("UML Attribute type cannot be empty!")

        return f"    {attribute.name} : {attribute.attr_type}"
