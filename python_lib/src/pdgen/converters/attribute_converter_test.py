from unittest.mock import MagicMock

import pytest

from pdgen.converters.attribute_converter import AttributeConverter
from pdgen.converters.services.uml_visibility_service import UMLVisibilityService
from pdgen.uml_types.types import UMLAttribute, UMLVisibility


def get_attribute_converter(visibility_convert_return_value: str) -> AttributeConverter:
    visibility_service: UMLVisibilityService = MagicMock()
    visibility_service.convert.return_value = visibility_convert_return_value
    return AttributeConverter(visibility_service)


def test_convert_simple_attribute():
    attribute_converter = get_attribute_converter("+")
    attribute = UMLAttribute(name="age", attr_type="int", visibility=UMLVisibility.PUBLIC)
    result = attribute_converter.convert(attribute)
    assert result == "    + age : int"


def test_convert_string_attribute():
    attribute_converter = get_attribute_converter("#")
    attribute = UMLAttribute(name="name", attr_type="string", visibility=UMLVisibility.PROTECTED)
    result = attribute_converter.convert(attribute)
    assert result == "    # name : string"


def test_convert_complex_type_attribute():
    attribute_converter = get_attribute_converter("-")

    attribute = UMLAttribute(name="address", attr_type="Address", visibility=UMLVisibility.PRIVATE)
    result = attribute_converter.convert(attribute)
    assert result == "    - address : Address"


def test_convert_empty_name_raises_error():
    attribute_converter = get_attribute_converter("-")
    attribute = UMLAttribute(name="", attr_type="string", visibility=UMLVisibility.PRIVATE)
    with pytest.raises(ValueError):
        attribute_converter.convert(attribute)


def test_convert_empty_type_raises_error():
    attribute_converter = get_attribute_converter("-")
    attribute = UMLAttribute(name="value", attr_type="", visibility=UMLVisibility.PRIVATE)
    with pytest.raises(ValueError):
        attribute_converter.convert(attribute)
