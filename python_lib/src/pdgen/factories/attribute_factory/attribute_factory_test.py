from unittest.mock import MagicMock

from pdgen.factories.attribute_factory.attribute_factory import AttributeFactory
from pdgen.factories.entities.type_info_collection import TypeInfoCollection
from pdgen.factories.entities.type_information import TypeInfo
from pdgen.factories.type_hints.type_hint_service import TypeHintService
from pdgen.uml_types.types import UMLAttribute, UMLVisibility


def get_side_effect_function(class_attrs: TypeInfoCollection, init_attrs: TypeInfoCollection):
    # pylint: disable=unused-argument
    def get_type_information_side_effect(target, *args, **kwargs):
        if target == object:
            return class_attrs
        if target == object.__init__:
            return init_attrs
        return TypeInfoCollection([])

    return get_type_information_side_effect


def test_get_all_attributes_distinct():
    type_hint_service: TypeHintService = MagicMock()

    class_attrs = TypeInfoCollection([
        TypeInfo("class_attr1", int),
        TypeInfo("class_attr2", str),
    ])
    init_attrs = TypeInfoCollection([
        TypeInfo("init_attr1", float),
        TypeInfo("init_attr2", bool),
    ])

    type_hint_service.get_type_infos.side_effect = get_side_effect_function(class_attrs,
                                                                            init_attrs)

    factory = AttributeFactory(type_hint_service=type_hint_service)

    result = factory.create_all(object)

    expected_attributes = [
        UMLAttribute("class_attr1", "int", visibility=UMLVisibility.PUBLIC),
        UMLAttribute("class_attr2", "str", visibility=UMLVisibility.PUBLIC),
        UMLAttribute("init_attr1", "float", visibility=UMLVisibility.PUBLIC),
        UMLAttribute("init_attr2", "bool", visibility=UMLVisibility.PUBLIC),
    ]
    assert result == expected_attributes


def test_class_attributes_empty():
    type_hint_service: TypeHintService = MagicMock()

    class_attrs = TypeInfoCollection([])
    init_attrs = TypeInfoCollection([
        TypeInfo("init_attr1", float),
        TypeInfo("init_attr2", bool),
    ])

    type_hint_service.get_type_infos.side_effect = get_side_effect_function(class_attrs,
                                                                            init_attrs)

    factory = AttributeFactory(type_hint_service=type_hint_service)

    result = factory.create_all(object)

    expected_attributes = [
        UMLAttribute("init_attr1", "float", visibility=UMLVisibility.PUBLIC),
        UMLAttribute("init_attr2", "bool", visibility=UMLVisibility.PUBLIC),
    ]
    assert result == expected_attributes


def test_same_names_in_class_and_init():
    type_hint_service: TypeHintService = MagicMock()

    class_attrs = TypeInfoCollection([
        TypeInfo("shared_attr", int),
        TypeInfo("class_attr1", str),
    ])
    init_attrs = TypeInfoCollection([
        TypeInfo("shared_attr", int),
        TypeInfo("init_attr1", bool),
    ])

    type_hint_service.get_type_infos.side_effect = (
        get_side_effect_function(class_attrs, init_attrs))

    factory = AttributeFactory(type_hint_service=type_hint_service)

    result = factory.create_all(object)

    expected_attributes = [
        UMLAttribute("shared_attr", "int", visibility=UMLVisibility.PUBLIC),
        UMLAttribute("class_attr1", "str", visibility=UMLVisibility.PUBLIC),
        UMLAttribute("init_attr1", "bool", visibility=UMLVisibility.PUBLIC),
    ]
    assert result == expected_attributes
