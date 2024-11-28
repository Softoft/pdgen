from unittest.mock import MagicMock

from pdgen.factories.attribute_factory.attribute_factory import AttributeFactory
from pdgen.factories.type_hints.type_information import TypeInfoCollection, TypeInformation
from pdgen.uml_types.types import UMLAttribute, UMLVisibility


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

    factory = AttributeFactory(type_hint_service=mock_type_hint_service)

    result = factory.create_all(object)

    expected_attributes = [
        UMLAttribute("class_attr1", "int", visibility=UMLVisibility.PUBLIC),
        UMLAttribute("class_attr2", "str", visibility=UMLVisibility.PUBLIC),
        UMLAttribute("init_attr1", "float", visibility=UMLVisibility.PUBLIC),
        UMLAttribute("init_attr2", "bool", visibility=UMLVisibility.PUBLIC),
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

    factory = AttributeFactory(type_hint_service=mock_type_hint_service)

    result = factory.create_all(object)

    expected_attributes = [
        UMLAttribute("init_attr1", "float", visibility=UMLVisibility.PUBLIC),
        UMLAttribute("init_attr2", "bool", visibility=UMLVisibility.PUBLIC),
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

    factory = AttributeFactory(type_hint_service=mock_type_hint_service)

    result = factory.create_all(object)

    expected_attributes = [
        UMLAttribute("shared_attr", "int", visibility=UMLVisibility.PUBLIC),
        UMLAttribute("class_attr1", "str", visibility=UMLVisibility.PUBLIC),
        UMLAttribute("init_attr1", "bool", visibility=UMLVisibility.PUBLIC),
    ]
    assert result == expected_attributes
