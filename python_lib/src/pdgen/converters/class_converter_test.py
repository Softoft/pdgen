# pylint: disable=redefined-outer-name
from unittest.mock import MagicMock

import pytest

from pdgen.converters.class_converter import ClassConverter
from pdgen.uml_types.types import UMLAttribute, UMLClass, UMLMethod, UMLVisibility


@pytest.fixture
def attribute_converter():
    return MagicMock()


@pytest.fixture
def method_converter():
    return MagicMock()


@pytest.fixture
def class_converter(attribute_converter, method_converter):
    return ClassConverter(attribute_converter, method_converter)


def test_convert_class_with_attributes_and_methods(class_converter,
                                                   attribute_converter,
                                                   method_converter):
    attribute1 = UMLAttribute(name="age", attr_type="int", visibility=UMLVisibility.PUBLIC)
    attribute2 = UMLAttribute(name="name", attr_type="string", visibility=UMLVisibility.PUBLIC)
    method1 = UMLMethod(name="getName",
                        parameters={},
                        return_type="string",
                        visibility=UMLVisibility.PUBLIC)
    method2 = UMLMethod(name="setAge",
                        parameters={"age": "int"},
                        return_type="void",
                        visibility=UMLVisibility.PUBLIC)

    uml_class = UMLClass(
        name="Person",
        _attributes=[attribute1, attribute2],
        _methods=[method1, method2],
    )

    attribute_converter.convert.side_effect = [
        "    + age : int",
        "    + name : string",
    ]
    method_converter.convert.side_effect = [
        "    + getName() : string",
        "    + setAge(age: int) : void",
    ]

    result = class_converter.convert(uml_class)

    assert result == [
        "class Person {",
        "    + age : int",
        "    + name : string",
        "    + getName() : string",
        "    + setAge(age: int) : void",
        "}",
    ]


def test_convert_class_with_no_attributes_or_methods(class_converter):
    uml_class = UMLClass(
        name="EmptyClass",
        _attributes=[],
        _methods=[],
    )

    result = class_converter.convert(uml_class)

    assert result == [
        "class EmptyClass {",
        "}",
    ]


def test_convert_class_raises_error_for_empty_name(class_converter):
    uml_class = UMLClass(
        name="",
        _attributes=[],
        _methods=[],
    )

    with pytest.raises(ValueError, match="UMLClass Name cant be empty!"):
        class_converter.convert(uml_class)


def test_convert_class_with_only_attributes(class_converter, attribute_converter):
    attribute1 = UMLAttribute(name="height", attr_type="float", visibility=UMLVisibility.PUBLIC)
    attribute2 = UMLAttribute(name="width", attr_type="float", visibility=UMLVisibility.PUBLIC)

    uml_class = UMLClass(
        name="Rectangle",
        _attributes=[attribute1, attribute2],
        _methods=[],
    )

    attribute_converter.convert.side_effect = [
        "    + height : float",
        "    + width : float",
    ]

    result = class_converter.convert(uml_class)

    assert result == [
        "class Rectangle {",
        "    + height : float",
        "    + width : float",
        "}",
    ]


def test_convert_class_with_only_methods(class_converter, method_converter):
    method1 = UMLMethod(name="draw",
                        parameters={},
                        return_type="void",
                        visibility=UMLVisibility.PRIVATE)
    method2 = UMLMethod(name="resize",
                        parameters={"factor": "float"},
                        return_type="void",
                        visibility=UMLVisibility.PRIVATE)

    uml_class = UMLClass(
        name="Drawable",
        _attributes=[],
        _methods=[method1, method2],
    )

    method_converter.convert.side_effect = [
        "    - draw() : void",
        "    - resize(factor: float) : void",
    ]

    result = class_converter.convert(uml_class)

    assert result == [
        "class Drawable {",
        "    - draw() : void",
        "    - resize(factor: float) : void",
        "}",
    ]
