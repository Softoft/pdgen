from types import NoneType

from src.services.type_hints.type_information import MethodSignature, TypeInformation


def some_method1(param1: str, param2: int, param3:bool) -> str:
    pass

def some_method2(param1: str, param2: int, param3):
    pass

class MyType:
    pass

def some_method3(param1: MyType, param2: list[tuple[int, str, MyType]]) -> None:
    pass


def test_get_type_hints(type_hint_service):
    type_information = type_hint_service.get_type_information(some_method1)
    assert type_information.return_type == str
    assert type_information.type_information_list == [
        TypeInformation('param1', str),
        TypeInformation('param2', int),
        TypeInformation('param3', bool)
    ]

def test_get_type_hints2(type_hint_service):
    type_information: MethodSignature = type_hint_service.get_type_information(some_method2)
    assert not type_information.has_return_type()
    assert type_information.return_type is None
    assert type_information.type_information_list == [
        TypeInformation('param1', str),
        TypeInformation('param2', int),
    ]

def test_get_type_hints3(type_hint_service):
    type_information: MethodSignature = type_hint_service.get_type_information(some_method3)
    assert type_information.has_return_type()
    assert type_information.return_type == NoneType
    assert type_information.type_information_list == [
        TypeInformation('param1', MyType),
        TypeInformation('param2', list[tuple[int, str, MyType]])
    ]