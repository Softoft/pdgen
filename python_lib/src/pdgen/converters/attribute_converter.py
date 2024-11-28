from pdgen.uml_types.types import UMLAttribute, UMLVisibility


class AttributeConverter:
    def _get_visibility_identifier(self, visibility: UMLVisibility) -> str:
        match visibility:
            case UMLVisibility.PUBLIC:
                return "+"
            case UMLVisibility.PROTECTED:
                return "#"
            case UMLVisibility.PRIVATE:
                return "-"
            case _:
                raise ValueError(f"Invalid visibility: {visibility}")

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

        visibility_identifier = self._get_visibility_identifier(attribute.visibility)
        return f"    {visibility_identifier} {attribute.name} : {attribute.attr_type}"
