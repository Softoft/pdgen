import enum
import inspect
from typing import get_type_hints


class UMLDiagramObject:
    pass


class UMLVisibility(enum.Enum):
    PUBLIC = enum.auto()
    PROTECTED = enum.auto()

    def get_plantuml_visibility_symbol(self) -> str:
        return {
            UMLVisibility.PUBLIC: '+',
            UMLVisibility.PROTECTED: '#',
        }[self]


class UMLAttribute(UMLDiagramObject):
    def __init__(self, name: str, _type: type = None, visibility: UMLVisibility = UMLVisibility.PUBLIC):
        self.name = name
        self.type = _type
        self.visibility = visibility


class UMLMethod(UMLDiagramObject):
    def __init__(self, name: str, return_type: type, parameters: list[type],
                 visibility: UMLVisibility = UMLVisibility.PUBLIC):
        self.name = name
        self.return_type = return_type
        self.parameters = parameters
        self.visibility = visibility


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

    def __init__(self, class_reference: type, display_name: str = None, auto_generate_methods: bool = True,
                 protected_method_identifier: str | bool = '_', private_method_identifier: str | bool = False):
        self.class_reference = class_reference
        self.display_name = display_name or class_reference.__name__
        self.auto_generate_methods = auto_generate_methods
        self.protected_method_identifier = protected_method_identifier
        self.private_method_identifier = private_method_identifier
        self.attributes: list[UMLAttribute] = []
        self.methods: list[UMLMethod] = []
        self.relations: set[UMLRelation] = set()

    def add_attribute(self, name: str, _type: type = None, visibility: UMLVisibility = UMLVisibility.PUBLIC):
        self.attributes.append(UMLAttribute(name, _type, visibility))

    def add_all_attributes(self):
        type_hints = get_type_hints(self.class_reference)

        init_signature = inspect.signature(self.class_reference.__init__)
        init_params = init_signature.parameters

        for param_name, param in init_params.items():
            if param_name == 'self' or param_name.startswith(self.EXCLUDE_ATTRIBUTES):
                continue
            param_type = type_hints.get(param_name, param.annotation)
            if param_type is inspect._empty:
                param_type = 'Any'
            else:
                param_type = param_type.__name__ if inspect.isclass(param_type) else str(param_type)

            visibility = UMLVisibility.PUBLIC if not param_name.startswith(
                self.protected_method_identifier) else UMLVisibility.PROTECTED
            self.add_attribute(param_name, param_type, visibility)

        for attr, attr_type in type_hints.items():
            if attr not in init_params and not attr.startswith(self.EXCLUDE_ATTRIBUTES):
                attr_type_name = attr_type.__name__ if inspect.isclass(attr_type) else str(attr_type)
                visibility = UMLVisibility.PUBLIC if not attr.startswith(
                    self.protected_method_identifier) else UMLVisibility.PROTECTED
                self.add_attribute(attr, attr_type_name, visibility)

    def add_method(self, name: str, return_type: type, parameters: list[type],
                   visibility: UMLVisibility = UMLVisibility.PUBLIC):
        self.methods.append(UMLMethod(name, return_type, parameters, visibility))

    def add_all_methods(self):
        specific_methods = getattr(self.class_reference, '__uml_methods', [])
        all_methods = inspect.getmembers(self.class_reference, predicate=inspect.isfunction)

        for name, method in all_methods:
            if not name.startswith('__'):
                if name.startswith(self.protected_method_identifier):
                    visibility = UMLVisibility.PROTECTED
                else:
                    visibility = UMLVisibility.PUBLIC

                if method in specific_methods or (not specific_methods and self.auto_generate_methods):
                    sig = inspect.signature(method)
                    return_type = sig.return_annotation
                    if return_type is inspect._empty:
                        return_type = None
                    else:
                        return_type = return_type.__name__ if inspect.isclass(return_type) else str(return_type)

                    parameters = []
                    for param_name, param in sig.parameters.items():
                        if param_name == 'self':
                            continue
                        param_type = param.annotation
                        if param_type is inspect._empty:
                            param_type = None
                        else:
                            param_type = param_type.__name__ if inspect.isclass(param_type) else str(param_type)
                        parameters.append((param_name, param_type))

                    self.add_method(name, return_type, parameters, visibility)

    def add_relationships(self):
        for base in self.class_reference.__bases__:
            if base.__name__ != 'object':
                self.relations.add(
                    UMLRelation(source=self.class_reference, target=base, relation_type=UMLRelationTypes.INHERITANCE))

        type_hints = get_type_hints(self.class_reference)
        for attr, attr_type in type_hints.items():
            if inspect.isclass(attr_type):
                self.relations.add(UMLRelation(source=self.class_reference, target=attr_type,
                                               relation_type=UMLRelationTypes.AGGREGATION))
