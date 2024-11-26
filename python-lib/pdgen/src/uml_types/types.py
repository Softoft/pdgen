import dataclasses


@dataclasses.dataclass(frozen=True)
class UMLAttribute:
    """
    A UML Attribute, which has a name and type.
    """
    name: str
    attr_type: str


@dataclasses.dataclass(frozen=True)
class UMLMethod:
    """
    A UML Method, which has a name, return type, and parameters.
    """
    name: str
    return_type: str
    parameters: dict[str, str]


@dataclasses.dataclass(frozen=True)
class UMLClass:
    """
    A UML Class, which has a name, attributes, and methods.
    """
    name: str
    attributes: list[UMLAttribute]
    methods: list[UMLMethod]


@dataclasses.dataclass(frozen=True)
class UMLDiagram:
    """
    A UML Diagram, which has a list of UML Classes.
    """
    classes: list[UMLClass]
