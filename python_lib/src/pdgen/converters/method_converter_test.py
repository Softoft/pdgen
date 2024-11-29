from unittest.mock import MagicMock

import pytest

from pdgen.converters.method_converter import MethodConverter
from pdgen.converters.services.uml_visibility_service import UMLVisibilityService
from pdgen.uml_types.types import UMLMethod, UMLVisibility


def get_method_converter(visibility_convert_return_value: str) -> MethodConverter:
    visibility_service: UMLVisibilityService = MagicMock()
    visibility_service.convert.return_value = visibility_convert_return_value
    return MethodConverter(visibility_service)


def test_convert_simple_method_with_return_type():
    method_converter = get_method_converter("+")
    method = UMLMethod(
        name="calculate",
        parameters={"x": "int", "y": "int"},
        return_type="int",
        visibility=UMLVisibility.PUBLIC,
    )
    result = method_converter.convert(method)
    assert result == "    + calculate(x: int, y: int) : int"


def test_convert_method_without_return_type():
    method_converter = get_method_converter("-")

    method = UMLMethod(
        name="printData",
        parameters={"data": "string"},
        return_type="",
        visibility=UMLVisibility.PRIVATE,
    )
    result = method_converter.convert(method)
    assert result == "    - printData(data: string)"


def test_convert_method_no_parameters_with_return_type():
    method_converter = get_method_converter("+")
    method = UMLMethod(
        name="getName",
        parameters={},
        return_type="string",
        visibility=UMLVisibility.PUBLIC
    )
    result = method_converter.convert(method)
    assert result == "    + getName() : string"


def test_convert_method_no_parameters_without_return_type():
    method_converter = get_method_converter("-")
    method = UMLMethod(
        name="initialize",
        parameters={},
        return_type="",
        visibility=UMLVisibility.PRIVATE
    )
    result = method_converter.convert(method)
    assert result == "    - initialize()"


def test_convert_method_empty_name_raises_error():
    method_converter = get_method_converter("-")
    method = UMLMethod(
        name="",
        parameters={"x": "int"},
        return_type="int",
        visibility=UMLVisibility.PRIVATE
    )
    with pytest.raises(ValueError):
        method_converter.convert(method)


def test_convert_method_empty_parameters():
    method_converter = get_method_converter("-")
    method = UMLMethod(
        name="doSomething",
        parameters={},
        return_type="None",
        visibility=UMLVisibility.PRIVATE
    )
    result = method_converter.convert(method)
    assert result == "    - doSomething() : None"


def test_convert_method_empty_return_type():
    method_converter = get_method_converter("-")
    method = UMLMethod(
        name="doSomething",
        parameters={},
        return_type="",
        visibility=UMLVisibility.PRIVATE
    )
    result = method_converter.convert(method)
    assert result == "    - doSomething()"
