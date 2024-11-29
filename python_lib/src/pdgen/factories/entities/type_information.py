import dataclasses

from pdgen.uml_types.types import UMLVisibility


@dataclasses.dataclass(frozen=True)
class TypeInfo:
    name: str
    type: type

    @property
    def visibility(self) -> UMLVisibility:
        return UMLVisibility.PRIVATE if self.name.startswith("_") else UMLVisibility.PUBLIC
