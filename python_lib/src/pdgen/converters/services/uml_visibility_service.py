from pdgen.uml_types.types import UMLVisibility


class UMLVisibilityService:
    def convert(self, uml_visibility: UMLVisibility) -> str:
        match uml_visibility:
            case UMLVisibility.PUBLIC:
                return "+"
            case UMLVisibility.PROTECTED:
                return "#"
            case UMLVisibility.PRIVATE:
                return "-"
            case _:
                raise ValueError(f"Invalid visibility: {uml_visibility}")
