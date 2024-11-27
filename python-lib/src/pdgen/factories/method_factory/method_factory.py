import dataclasses
import inspect
import typing

from pdgen.factories.type_hints.type_hint_service import TypeHintService
from pdgen.factories.type_hints.type_information import MethodSignature
from pdgen.uml_types.types import UMLMethod


@dataclasses.dataclass(frozen=True)
class MethodInformation:
    name: str
    function_reference: object


class MethodFactory:
    def __init__(self, type_hint_service: TypeHintService):
        self._type_hint_service: TypeHintService = type_hint_service

    def _find_all_methods(self, class_reference) -> list[MethodInformation]:
        return [MethodInformation(func_name, func_ref) for func_name, func_ref
                in inspect.getmembers(class_reference, inspect.isfunction)]

    def _find_all_uml_methods(self, class_reference) -> list[MethodInformation]:
        all_methods = self._find_all_methods(class_reference)
        for method in all_methods:
            print(method.function_reference.__name__)
            print(hasattr(method.function_reference, '__is_uml_method__'))
        return [method for method in all_methods if
                hasattr(method.function_reference, '__is_uml_method__')]
    def _method_params_as_dict(self, method_signature: MethodSignature):
        return {param.name: param.type.__name__ for param in method_signature.type_information_list}

    def create_all(self, class_reference) -> list[UMLMethod]:
        print(f"All Methods: {self._find_all_methods(class_reference)}")
        uml_methods = self._find_all_uml_methods(class_reference)
        print(f"UML methods: {uml_methods}")

        all_methods: list[UMLMethod] = []
        for method in uml_methods:
            type_hints = self._type_hint_service.get_type_information(method.function_reference)
            method_signature: MethodSignature = typing.cast(MethodSignature, type_hints)
            method_params: dict[str, str] = self._method_params_as_dict(method_signature)
            all_methods.append(UMLMethod(method.name,
                                         method_signature.get_return_type_as_str(),
                                         method_params))
        return all_methods

def create_uml_method_factory() -> MethodFactory:
    type_hint_service = TypeHintService()
    return MethodFactory(type_hint_service)