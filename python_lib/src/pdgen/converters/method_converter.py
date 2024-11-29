from pdgen.converters.services.uml_visibility_service import UMLVisibilityService
from pdgen.uml_types.types import UMLMethod


class MethodConverter:
    def __init__(self, uml_visibility_service: UMLVisibilityService):
        self._uml_visibility_service = uml_visibility_service

    def convert(self, method: UMLMethod) -> str:
        """
        Converts a UMLMethod to PlantUML format.

        Args:
            method (UMLMethod): The method_factory to convert.

        Returns:
            str: PlantUML representation of the method_factory.
        """
        if not method.name:
            raise ValueError("UML Methods name cant be empty!")

        parameter_list = ", ".join(
            f"{param}: {ptype}" for param, ptype in method.parameters.items()
        )

        visibility: str = self._uml_visibility_service.convert(method.visibility)
        if method.return_type:
            return f"    {visibility} {method.name}({parameter_list}) : {method.return_type}"
        return f"    {visibility} {method.name}({parameter_list})"
