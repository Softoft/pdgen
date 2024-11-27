import pytest
from pdgen.uml_types.types import UMLAttribute
from pdgen.converters.attribute_converter import AttributeConverter


@pytest.fixture
def attribute_converter():
    return AttributeConverter()


def test_convert_simple_attribute(attribute_converter):
    attribute = UMLAttribute(name="age", attr_type="int")
    result = attribute_converter.convert(attribute)
    assert result == "    age : int"


def test_convert_string_attribute(attribute_converter):
    attribute = UMLAttribute(name="name", attr_type="string")
    result = attribute_converter.convert(attribute)
    assert result == "    name : string"


def test_convert_complex_type_attribute(attribute_converter):
    attribute = UMLAttribute(name="address", attr_type="Address")
    result = attribute_converter.convert(attribute)
    assert result == "    address : Address"


def test_convert_empty_name_raises_error(attribute_converter):
    attribute = UMLAttribute(name="", attr_type="string")
    with pytest.raises(ValueError):
        attribute_converter.convert(attribute)


def test_convert_empty_type_raises_error(attribute_converter):
    attribute = UMLAttribute(name="value", attr_type="")
    with pytest.raises(ValueError):
        attribute_converter.convert(attribute)
