import pytest

from src.services.type_hints.type_hint_service import TypeHintService

@pytest.fixture
def type_hint_service():
    return TypeHintService()
