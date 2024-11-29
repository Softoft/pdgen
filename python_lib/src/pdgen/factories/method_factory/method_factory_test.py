from unittest.mock import MagicMock, patch

from pdgen.factories.entities.method_signature import MethodSignature
from pdgen.factories.entities.type_information import TypeInfo
from pdgen.factories.method_factory.method_factory import MethodFactory
from pdgen.factories.type_hints.type_hint_service import TypeHintService
from pdgen.uml_types.types import UMLMethod, UMLVisibility


def test_uml_method_factory_without_extra_service():
    mock_type_hint_service: TypeHintService = MagicMock()

    mock_method_signature = MethodSignature([
        TypeInfo(name="param1", type=str),
        TypeInfo(name="param2", type=int),
        TypeInfo(name="return", type=bool),
    ])
    mock_type_hint_service.get_type_infos.return_value = mock_method_signature

    with patch("inspect.getmembers") as mock_getmembers:
        # pylint: disable=unused-argument
        def mock_method(x: str, y: int) -> bool:
            pass

        mock_method.__is_uml_method__ = True
        mock_methods = [
            ("mock_method", mock_method),
        ]
        mock_getmembers.return_value = mock_methods

        factory = MethodFactory(type_hint_service=mock_type_hint_service)

        result = factory.create_all(class_reference=object)

        expected_result = [
            UMLMethod(
                name="mock_method",
                return_type="bool",
                parameters={"param1": "str", "param2": "int"},
                visibility=UMLVisibility.PUBLIC
            ),
        ]

        assert result == expected_result
