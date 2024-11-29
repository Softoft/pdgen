from pdgen.converters.services.uml_visibility_service import UMLVisibilityService
from pdgen.uml_types.types import UMLAttribute


class AttributeConverter:
    def __init__(self, uml_visibility_service: UMLVisibilityService):
        self._uml_visibility_service = uml_visibility_service


    def convert(self, attribute: UMLAttribute) -> str:
        """
        Converts an UMLAttribute to PlantUML format.

        Args:
            attribute (UMLAttribute): The attribute to convert.

        Returns:
            str: PlantUML representation of the attribute.

        Raises:
            ValueError: If the attribute's name or type is empty.
        """
        if not attribute.name:
            raise ValueError("UML Attribute name cannot be empty!")
        if not attribute.attr_type:
            raise ValueError("UML Attribute type cannot be empty!")

        visibility_identifier = self._uml_visibility_service.convert(attribute.visibility)
        return f"    {visibility_identifier} {attribute.name} : {attribute.attr_type}"
