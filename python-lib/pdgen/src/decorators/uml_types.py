import dataclasses
import enum
import typing


class UMLDiagramObject:
    pass


class UMLVisibility(enum.Enum):
    PUBLIC = enum.auto()
    PROTECTED = enum.auto()


@dataclasses.dataclass
class UMLAttribute(UMLDiagramObject):
    name: str
    attr_type: type
    visibility: UMLVisibility = UMLVisibility.PUBLIC


@dataclasses.dataclass
class UMLMethod(UMLDiagramObject):
    name: str
    return_type: type
    parameters: dict[str, type]
    visibility: UMLVisibility = UMLVisibility.PUBLIC


class UMLRelationTypes(enum.Enum):
    AGGREGATION = enum.auto()
    INHERITANCE = enum.auto()
    DEPENDENCY = enum.auto()

    def get_plantuml_relation_symbol(self) -> str:
        return {
            UMLRelationTypes.AGGREGATION: 'o--',
            UMLRelationTypes.INHERITANCE: '--|>',
            UMLRelationTypes.DEPENDENCY: '-->'
        }[self]


class UMLRelation(UMLDiagramObject):
    def __init__(self, source: type, target: type, relation_type: UMLRelationTypes):
        self.source = source
        self.target = target
        self.relation_type = relation_type

    def get_plantuml_relation(self) -> str:
        return f'{self.source.__name__} {self.relation_type.get_plantuml_relation_symbol()} {self.target.__name__}'

    def __eq__(self, other):
        return self.source == other.source and self.target == other.target and self.relation_type == other.relation_type

    def __hash__(self):
        return hash((self.source, self.target, self.relation_type))


class UMLClass(UMLDiagramObject):
    EXCLUDE_ATTRIBUTES = '__'
    PROTECTED_METHOD_IDENTIFIER = '_'

    def __init__(self, class_reference: type):
        self.class_reference = class_reference
        self.display_name = class_reference.__name__
        self.attributes: list[UMLAttribute] = []
        self.methods: list[UMLMethod] = []
        self.relations: set[UMLRelation] = set()

    def add_attribute(self, name: str, _type: type, visibility=UMLVisibility.PUBLIC):
        self.attributes.append(UMLAttribute(name, _type, visibility))

    def add_all_attributes(self):
        class_attrs: dict[str, type] = typing.get_type_hints(self.class_reference)
        init_attrs: dict[str, type] = typing.get_type_hints(self.class_reference.__init__)

        union_attrs = {**class_attrs, **init_attrs}
        filtered_attrs: dict[str, type] = {k: v for k, v in union_attrs.items()
                                           if not k.startswith(self.EXCLUDE_ATTRIBUTES)
                                           and k not in ['return', 'self']}
        for param_name, param_type in filtered_attrs.items():
            self.add_attribute(param_name, param_type)

    def add_method(self, name: str, return_type: type, parameters: dict[str, type],
                   visibility=UMLVisibility.PUBLIC):
        self.methods.append(UMLMethod(name, return_type, parameters, visibility))

    def add_all_methods(self):
        specific_methods: list[object] = getattr(self.class_reference, '__uml_methods', [])
        filtered_methods = [method for method in specific_methods if
                            not method.__name__.startswith(self.EXCLUDE_ATTRIBUTES)]
        for method in filtered_methods:
            method_signature: dict[str, type] = typing.get_type_hints(method)
            return_type = method_signature.pop('return', type(None))
            method_signature.pop('self')

            # noinspection PyTypeChecker
            self.add_method(name=method.__name__,
                            return_type=return_type,
                            parameters=method_signature)
