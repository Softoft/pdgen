import dataclasses
import enum


class UMLVisibility(enum.Enum):
    """
    An enumeration of the possible visibilities of a UML element.
    """
    PUBLIC = "public"
    PROTECTED = "protected"
    PRIVATE = "private"

@dataclasses.dataclass(frozen=True)
class UMLAttribute:
    """
    A UML Attribute, which has a name and type.
    """
    name: str
    attr_type: str
    visibility: UMLVisibility

    def __eq__(self, other):
        if not isinstance(other, UMLAttribute):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


@dataclasses.dataclass(frozen=True)
class UMLMethod:
    """
    An UML Method

    Attributes:
        name (str): The name of the method_factory.
        return_type (str): The type of value returned by the method_factory.
        parameters (Dict[str, str]): A dictionary of the method_factory's parameters, where:
            - Keys are the names of the parameters (e.g., "num").
            - Values are the types of the parameters as strings (e.g., "int").

    """
    name: str
    return_type: str
    parameters: dict[str, str]
    visibility: UMLVisibility

    def __eq__(self, other):
        if not isinstance(other, UMLMethod):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


@dataclasses.dataclass(frozen=True)
class UMLClass:
    """
    A UML Class, which has a name, _attributes, and _methods.
    """
    name: str
    _attributes: list[UMLAttribute]
    _methods: list[UMLMethod]

    @property
    def attributes(self):
        return list(dict.fromkeys(self._attributes))

    @property
    def methods(self):
        return list(dict.fromkeys(self._methods))

    def __eq__(self, other):
        if not isinstance(other, UMLClass):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)




@dataclasses.dataclass(frozen=True)
class UMLDiagram:
    """
    A UML Diagram, which has a list of UML Classes.
    """
    classes: frozenset[UMLClass]
