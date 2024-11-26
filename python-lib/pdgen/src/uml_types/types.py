import dataclasses


@dataclasses.dataclass
class UMLAttribute(frozen=True):
    name: str
    attr_type: type


@dataclasses.dataclass
class UMLMethod(frozen=True):
    name: str
    return_type: type
    parameters: dict[str, type]


@dataclasses.dataclass(frozen=True)
class UMLClass:
    name: str
    attributes: list[UMLAttribute]
    methods: list[UMLMethod]


@dataclasses.dataclass(frozen=True)
class UMLDiagram:
    classes: list[UMLClass]
