from unittest.mock import MagicMock
from src.services.uml_attribute_factory import UMLAttributeFactory
from src.services.type_hints.type_information import TypeInfoCollection, TypeInformation
from src.uml_types.types import UMLAttribute


def get_side_effect_function(class_attrs: TypeInfoCollection, init_attrs: TypeInfoCollection):
    def get_type_information_side_effect(target, *args):
        if target == object:
            return class_attrs
        elif target == object.__init__:
            return init_attrs
        else:
            return TypeInfoCollection([])
    return get_type_information_side_effect


def test_get_all_attributes_distinct():
    mock_type_hint_service = MagicMock()

    class_attrs = TypeInfoCollection([
        TypeInformation("class_attr1", int),
        TypeInformation("class_attr2", str),
    ])
    init_attrs = TypeInfoCollection([
        TypeInformation("init_attr1", float),
        TypeInformation("init_attr2", bool),
    ])

    mock_type_hint_service.get_type_information.side_effect = get_side_effect_function(class_attrs, init_attrs)

    factory = UMLAttributeFactory(type_hint_service=mock_type_hint_service)

    result = factory.create_all(object)

    expected_attributes = [
        UMLAttribute("class_attr1", "int"),
        UMLAttribute("class_attr2", "str"),
        UMLAttribute("init_attr1", "float"),
        UMLAttribute("init_attr2", "bool"),
    ]
    assert result == expected_attributes


def test_class_attributes_empty():
    mock_type_hint_service = MagicMock()

    class_attrs = TypeInfoCollection([])
    init_attrs = TypeInfoCollection([
        TypeInformation("init_attr1", float),
        TypeInformation("init_attr2", bool),
    ])

    mock_type_hint_service.get_type_information.side_effect = get_side_effect_function(class_attrs, init_attrs)

    factory = UMLAttributeFactory(type_hint_service=mock_type_hint_service)

    result = factory.create_all(object)

    expected_attributes = [
        UMLAttribute("init_attr1", "float"),
        UMLAttribute("init_attr2", "bool"),
    ]
    assert result == expected_attributes


def test_same_names_in_class_and_init():
    mock_type_hint_service = MagicMock()

    class_attrs = TypeInfoCollection([
        TypeInformation("shared_attr", int),
        TypeInformation("class_attr1", str),
    ])
    init_attrs = TypeInfoCollection([
        TypeInformation("shared_attr", int),
        TypeInformation("init_attr1", bool),
    ])

    mock_type_hint_service.get_type_information.side_effect = get_side_effect_function(class_attrs, init_attrs)

    factory = UMLAttributeFactory(type_hint_service=mock_type_hint_service)

    result = factory.create_all(object)

    expected_attributes = [
        UMLAttribute("shared_attr", "int"),
        UMLAttribute("class_attr1", "str"),
        UMLAttribute("init_attr1", "bool"),
    ]
    assert result == expected_attributes
