from types import NoneType

from pdgen.factories.entities.method_signature import MethodSignature
from pdgen.factories.entities.type_information import TypeInfo


# pylint: disable=unused-argument
def some_method1(param1: str, param2: int, param3: bool) -> str:
    pass


# pylint: disable=unused-argument
def some_method2(param1: str, param2: int, param3):
    pass


class MyType:
    pass


# pylint: disable=unused-argument
def some_method3(param1: MyType, param2: list[tuple[int, str, MyType]]) -> None:
    pass


class MyTest:
    def __init__(self, param1: str, param2: int):
        pass


def test_function_full_type_hints(type_hint_service):
    type_information = type_hint_service.get_type_infos(some_method1)
    assert type_information.return_type == str
    assert type_information.type_information_list == [
        TypeInfo('param1', str),
        TypeInfo('param2', int),
        TypeInfo('param3', bool)
    ]


def test_no_return_type(type_hint_service):
    type_information: MethodSignature = type_hint_service.get_type_infos(some_method2)
    assert not type_information.has_return_type()
    assert type_information.return_type is None
    assert type_information.type_information_list == [
        TypeInfo('param1', str),
        TypeInfo('param2', int),
    ]


def test_complex_type(type_hint_service):
    type_information: MethodSignature = type_hint_service.get_type_infos(some_method3)
    assert type_information.has_return_type()
    assert type_information.return_type == NoneType
    assert type_information.type_information_list == [
        TypeInfo('param1', MyType),
        TypeInfo('param2', list[tuple[int, str, MyType]])
    ]


def test_init_method(type_hint_service):
    type_information: MethodSignature = type_hint_service.get_type_infos(MyTest.__init__)
    assert not type_information.has_return_type()
    assert type_information.return_type is None
    assert type_information.type_information_list == [
        TypeInfo('param1', str),
        TypeInfo('param2', int),
    ]
