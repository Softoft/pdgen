# pylint: disable=redefined-outer-name
import pytest

from pdgen.decorators.uml_decorators import include_in_uml
from pdgen.repositories.class_repository import ClassRepository


@pytest.fixture(scope="function")
def uml_class_repository():
    repo = ClassRepository.get_instance()
    repo.clear()
    return repo


def test_class_inclusion(uml_class_repository):
    assert uml_class_repository.get_all() == []

    @include_in_uml
    class TestClass:
        def method1(self):
            pass

    assert TestClass in uml_class_repository
    assert not hasattr(TestClass, "__is_uml_method__")


def test_method_inclusion(uml_class_repository):
    assert uml_class_repository.get_all() == []

    @include_in_uml
    class TestClass:
        @include_in_uml
        def method1(self):
            pass

    assert TestClass in uml_class_repository

    assert hasattr(TestClass.method1, "__is_uml_method__")
    assert getattr(TestClass.method1, "__is_uml_method__")


def test_non_included_class_method_error(uml_class_repository):
    assert uml_class_repository.get_all() == []

    class TestClass:
        @include_in_uml
        def method1(self):
            pass

    assert TestClass not in uml_class_repository
    assert hasattr(TestClass.method1, "__is_uml_method__")
    assert getattr(TestClass.method1, "__is_uml_method__")
