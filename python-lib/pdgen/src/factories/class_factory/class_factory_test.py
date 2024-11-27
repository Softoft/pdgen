from unittest.mock import MagicMock

from src.factories.class_factory import UMLClassFactory
from src.uml_types.types import UMLAttribute, UMLClass, UMLMethod


def test_uml_method_factory_without_extra_service():
    mock_attribute_factory = MagicMock()
    mock_method_factory = MagicMock()

    uml_methods = [
        UMLMethod(
            name="mock_method",
            return_type="bool",
            parameters={"param1": "str", "param2": "int"},
        ),

    ]

    uml_attributes = [
        UMLAttribute("class_attr1", "int"),
        UMLAttribute("class_attr2", "str"),
        UMLAttribute("init_attr1", "float"),
        UMLAttribute("init_attr2", "bool"),
    ]

    mock_method_factory.create_all.return_value = uml_methods
    mock_attribute_factory.create_all.return_value = uml_attributes

    class TestClass:
        pass

    factory = UMLClassFactory(attribute_factory=mock_attribute_factory,
                              method_factory=mock_method_factory)

    result = factory.create_uml_class(TestClass)

    expected_result = UMLClass("TestClass", uml_attributes, uml_methods)

    assert result == expected_result
