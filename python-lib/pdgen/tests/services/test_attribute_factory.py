from unittest.mock import MagicMock

from src.services.uml_attribute_factory import UMLAttributeFactory
from src.services.type_hints.type_information import TypeInfoCollection, TypeInformation
from src.uml_types.types import UMLAttribute


def test_get_all_attributes():
    # Mock TypeHintService
    mock_type_hint_service = MagicMock()

    # Mock TypeInfoCollection for class attributes and __init__ method
    mock_class_attrs = TypeInfoCollection([
        TypeInformation("class_attr1", int),
        TypeInformation("class_attr2", str),
    ])
    mock_init_attrs = TypeInfoCollection([
        TypeInformation("init_attr1", float),
        TypeInformation("init_attr2", bool),
    ])

    mock_type_hint_service.get_type_information.side_effect = [mock_class_attrs, mock_init_attrs]

    # Create UMLAttributeFactory with the mocked service
    factory = UMLAttributeFactory(type_hint_service=mock_type_hint_service)

    # Test get_all_attributes
    result = factory.create_all(object)  # Replace 'object' with your class

    # Assertions
    expected_attributes = [
        UMLAttribute("class_attr1", "int"),
        UMLAttribute("class_attr2", "str"),
        UMLAttribute("init_attr1", "float"),
        UMLAttribute("init_attr2", "bool"),
    ]
    assert set(result) == set(expected_attributes)