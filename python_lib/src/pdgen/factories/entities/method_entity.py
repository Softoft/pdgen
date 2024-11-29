import dataclasses

from pdgen.uml_types.types import UMLVisibility


@dataclasses.dataclass(frozen=True)
class MethodInformation:
    name: str
    function_reference: object

    @property
    def visibility(self) -> UMLVisibility:
        return UMLVisibility.PRIVATE if self.name.startswith("_") else UMLVisibility.PUBLIC
