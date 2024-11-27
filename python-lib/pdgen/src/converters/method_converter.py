from src.uml_types.types import UMLMethod


class MethodConverter:
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
        if method.return_type:
            return f"    {method.name}({parameter_list}) : {method.return_type}"
        return f"    {method.name}({parameter_list})"
