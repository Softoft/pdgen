import pytest

from src.repositories.class_repository import ClassRepository


def test_class_repository_add():
    class TestClass1:
        pass
    class_repo = ClassRepository()
    class_repo.clear()
    assert class_repo.get_all() == []
    class_repo.add(TestClass1)
    assert class_repo.get_all() == [TestClass1]

def test_class_repository_add_only_allow_classes():
    class TestClass1:
        pass
    class_repo = ClassRepository()
    class_repo.clear()
    assert class_repo.get_all() == []
    class_repo.add(TestClass1)
    assert class_repo.get_all() == [TestClass1]
    with pytest.raises(ValueError):
        # noinspection PyTypeChecker
        class_repo.add(TestClass1())

    with pytest.raises(ValueError):
        class_repo.add(str)

def test_class_repository_is_singleton():
    class_repo1 = ClassRepository()
    class_repo2 = ClassRepository()
    assert class_repo1 is class_repo2


def test_class_repository_clear():
    class TestClass1:
        pass
    class_repo = ClassRepository()
    class_repo.clear()
    assert class_repo.get_all() == []
    class_repo.add(TestClass1)
    assert class_repo.get_all() == [TestClass1]
    class_repo.clear()
    assert class_repo.get_all() == []