from src.uml_types.types import UMLMethod


class PlantUMLMethodConverter:
    def convert(self, method: UMLMethod) -> str:
        """
        Converts a UMLMethod to PlantUML format.

        Args:
            method (UMLMethod): The method to convert.

        Returns:
            str: PlantUML representation of the method.
        """
        parameter_list = ", ".join(
            f"{param}: {ptype}" for param, ptype in method.parameters.items()
        )
        return f"    {method.name}({parameter_list}) : {method.return_type}"