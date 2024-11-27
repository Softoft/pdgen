from unittest.mock import MagicMock
import pytest
from src.converters.diagram_converter import DiagramConverter
from src.uml_types.types import UMLDiagram, UMLClass


@pytest.fixture
def class_converter():
    return MagicMock()


@pytest.fixture
def diagram_converter(class_converter):
    return DiagramConverter(class_converter)


def normalize_plantuml(output: str) -> str:
    """
    Normalize the PlantUML output by removing all blank lines.
    """
    return "\n".join(line for line in output.splitlines() if line.strip())


def test_convert_diagram_with_multiple_classes(diagram_converter, class_converter):
    uml_class1 = UMLClass(name="Person", _attributes=[], _methods=[])
    uml_class2 = UMLClass(name="Rectangle", _attributes=[], _methods=[])
    uml_diagram = UMLDiagram(classes=frozenset([uml_class1, uml_class2]))

    class_converter.convert.side_effect = [
        ["class Person {", "}"],
        ["class Rectangle {", "}"],
    ]

    result = diagram_converter.convert(uml_diagram)

    expected_output = (
        "@startuml\n"
        "skinparam dpi 600\n"
        "class Person {\n"
        "}\n"
        "class Rectangle {\n"
        "}\n"
        "@enduml"
    )
    assert normalize_plantuml(result) == normalize_plantuml(expected_output)


def test_convert_diagram_with_single_class(diagram_converter, class_converter):
    uml_class = UMLClass(name="Person", _attributes=[], _methods=[])
    uml_diagram = UMLDiagram(classes=frozenset([uml_class]))

    class_converter.convert.return_value = [
        "class Person {",
        "    age : int",
        "    getName() : string",
        "}"
    ]

    result = diagram_converter.convert(uml_diagram)

    expected_output = (
        "@startuml\n"
        "skinparam dpi 600\n"
        "class Person {\n"
        "    age : int\n"
        "    getName() : string\n"
        "}\n"
        "@enduml"
    )
    assert normalize_plantuml(result) == normalize_plantuml(expected_output)


def test_convert_empty_diagram(diagram_converter):
    uml_diagram = UMLDiagram(classes=frozenset())

    result = diagram_converter.convert(uml_diagram)

    expected_output = (
        "@startuml\n"
        "skinparam dpi 600\n"
        "@enduml"
    )
    assert normalize_plantuml(result) == normalize_plantuml(expected_output)


def test_convert_diagram_with_class_converter_error(diagram_converter, class_converter):
    uml_class = UMLClass(name="InvalidClass", _attributes=[], _methods=[])
    uml_diagram = UMLDiagram(classes=frozenset([uml_class]))

    class_converter.convert.side_effect = RuntimeError("Conversion error")

    with pytest.raises(RuntimeError, match="Conversion error"):
        diagram_converter.convert(uml_diagram)
