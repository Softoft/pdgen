import dataclasses
import enum
import inspect
import typing


class UMLDiagramObject:
    pass



@dataclasses.dataclass
class UMLAttribute(UMLDiagramObject):
    name: str
    attr_type: type


@dataclasses.dataclass
class UMLMethod(UMLDiagramObject):
    name: str
    return_type: type
    parameters: dict[str, type]

@dataclasses.dataclass
class TypeInformation:
    name: str
    type: type

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

@dataclasses.dataclass
class MethodInformation:
    name: str
    function_reference: object

def get_type_hint_information(_object: object) -> list[TypeInformation]:
    type_hints = typing.get_type_hints(_object)
    return [TypeInformation(name, _type) for name, _type in type_hints.items()]


class UMLClass(UMLDiagramObject):
    EXCLUDE_ATTRIBUTES = '__'
    PROTECTED_METHOD_IDENTIFIER = '_'

    def __init__(self, class_reference: type):
        self.class_reference = class_reference
        self.display_name = class_reference.__name__
        self.attributes: list[UMLAttribute] = []
        self.methods: list[UMLMethod] = []

    def _is_attribute_excluded(self, type_info: TypeInformation) -> bool:
        return type_info.name.startswith(self.EXCLUDE_ATTRIBUTES)

    def _is_method_excluded(self, method_name: str) -> bool:
        return method_name.startswith(self.EXCLUDE_ATTRIBUTES)

    def _find_all_methods(self) -> list[MethodInformation]:
        return [MethodInformation(func_name, func_ref) for func_name, func_ref
                in inspect.getmembers(self.class_reference, inspect.isfunction)]

    def _find_all_uml_methods(self) -> list[MethodInformation]:
        all_methods = self._find_all_methods()
        for method in all_methods:
            print(method.function_reference.__name__)
            print(hasattr(method.function_reference, '__is_uml_method__'))
        return [method for method in all_methods if hasattr(method.function_reference, '__is_uml_method__')]

    def add_attribute(self, type_info: TypeInformation):
        self.attributes.append(UMLAttribute(type_info.name, type_info.type))

    def add_all_attributes(self):
        class_attrs: list[TypeInformation] = get_type_hint_information(self.class_reference)
        init_attrs: list[TypeInformation] = get_type_hint_information(self.class_reference.__init__)
        print(init_attrs)
        print(class_attrs)
        union_attrs: list[TypeInformation] = list(set(class_attrs) | set(init_attrs))
        print(f"union:  {union_attrs}")
        filtered_attrs: list[TypeInformation] = list(filter(
            lambda x: not self._is_attribute_excluded(x), union_attrs))
        print(filtered_attrs)
        for type_info in filtered_attrs:
            self.add_attribute(type_info)

    def add_method(self, name: str, return_type: type, parameters: dict[str, type]):
        self.methods.append(UMLMethod(name, return_type, parameters))

    def add_all_methods(self):
        print(f"All Methods: {self._find_all_methods()}")
        uml_methods = self._find_all_uml_methods()
        print(f"UML methods: {uml_methods}")
        for method in uml_methods:
            method_signature: dict[str, type] = typing.get_type_hints(method.function_reference)
            return_type = method_signature.pop('return', type(None))

            # noinspection PyTypeChecker
            self.add_method(name=method.name,
                            return_type=return_type,
                            parameters=method_signature)
