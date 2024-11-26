from unittest.mock import MagicMock, patch
from src.services.type_hints.type_information import MethodSignature, TypeInformation
from src.services.uml_method_factory import UMLMethodFactory
from src.uml_types.types import UMLMethod


def test_uml_method_factory_without_extra_service():
    # Step 1: Mock TypeHintService
    mock_type_hint_service = MagicMock()

    # Mock return value of `get_type_information`
    mock_method_signature = MethodSignature([
        TypeInformation(name="param1", type=str),
        TypeInformation(name="param2", type=int),
        TypeInformation(name="return", type=bool),
    ])
    mock_type_hint_service.get_type_information.return_value = mock_method_signature

    # Step 2: Patch `inspect.getmembers`
    with patch("inspect.getmembers") as mock_getmembers:
        def mock_method(x: str, y: int) -> bool:
            pass

        mock_method.__is_uml_method__ = True
        mock_methods = [
            ("mock_method", mock_method),
        ]
        mock_getmembers.return_value = mock_methods

        # Step 3: Create UMLMethodFactory with the mocked TypeHintService
        factory = UMLMethodFactory(type_hint_service=mock_type_hint_service)

        # Step 4: Test `get_all_methods`
        result = factory.create_all(class_reference=object)

        # Step 5: Define the expected output
        expected_result = [
            UMLMethod(
                name="mock_method",
                return_type="bool",
                parameters={"param1": "str", "param2": "int"},
            ),
        ]

        assert result == expected_result