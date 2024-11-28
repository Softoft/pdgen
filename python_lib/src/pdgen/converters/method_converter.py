from pdgen.uml_types.types import UMLMethod, UMLVisibility


class MethodConverter:
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

        visibility_identifier = self._get_visibility_identifier(method.visibility)
        if method.return_type:
            return f"    {visibility_identifier} {method.name}({parameter_list}) : {method.return_type}"
        return f"    {visibility_identifier} {method.name}({parameter_list})"
