from unittest.mock import MagicMock

from pdgen.factories.class_factory.class_factory import ClassFactory
from pdgen.uml_types.types import UMLAttribute, UMLClass, UMLMethod, UMLVisibility


def test_uml_method_factory_without_extra_service():
    mock_attribute_factory = MagicMock()
    mock_method_factory = MagicMock()

    uml_methods = [
        UMLMethod(
            name="mock_method",
            return_type="bool",
            parameters={"param1": "str", "param2": "int"},
            visibility=UMLVisibility.PUBLIC
        ),

    ]

    uml_attributes = [
        UMLAttribute("class_attr1", "int", visibility=UMLVisibility.PUBLIC),
        UMLAttribute("class_attr2", "str", visibility=UMLVisibility.PUBLIC),
        UMLAttribute("init_attr1", "float", visibility=UMLVisibility.PUBLIC),
        UMLAttribute("init_attr2", "bool", visibility=UMLVisibility.PUBLIC),
    ]

    mock_method_factory.create_all.return_value = uml_methods
    mock_attribute_factory.create_all.return_value = uml_attributes

    class TestClass:
        pass

    factory = ClassFactory(attribute_factory=mock_attribute_factory,
                           method_factory=mock_method_factory)

    result = factory.create_uml_class(TestClass)

    expected_result = UMLClass(TestClass.__name__, uml_attributes, uml_methods)

    assert result == expected_result
