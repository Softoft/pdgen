from unittest.mock import MagicMock

from pdgen.factories.class_factory.class_factory import ClassFactory
from pdgen.factories.diagram_factory.diagram_factory import DiagramFactory
from pdgen.repositories.class_repository import ClassRepository
from pdgen.uml_types.types import UMLClass, UMLDiagram


def create_mock_uml_class_factory(return_mapping: dict) -> ClassFactory:
    mock_uml_class_factory: ClassFactory = MagicMock()

    def side_effect(param):
        return return_mapping.get(param, None)

    mock_uml_class_factory.create_uml_class.side_effect = side_effect
    return mock_uml_class_factory


def create_mock_class_repository(classes) -> ClassRepository:
    mock_class_repository: ClassRepository = MagicMock()
    mock_class_repository.get_all.return_value = classes
    return mock_class_repository


def test_uml_class_factory_mock():
    class TestClass1:
        pass

    class TestClass2:
        pass

    class TestClass3:
        pass

    mock_uml_class1 = UMLClass("TestClass1", [], [])
    mock_uml_class2 = UMLClass("TestClass2", [], [])

    return_mapping = {
        TestClass1: mock_uml_class1,
        TestClass2: mock_uml_class2,
    }

    mock_uml_class_factory = create_mock_uml_class_factory(return_mapping)

    result1 = mock_uml_class_factory.create_uml_class(TestClass1)
    result2 = mock_uml_class_factory.create_uml_class(TestClass2)
    result3 = mock_uml_class_factory.create_uml_class(TestClass3)

    assert result1 == mock_uml_class1
    assert result2 == mock_uml_class2
    assert result3 is None


def test_class_repository_mock():
    class TestClass1:
        pass

    class TestClass2:
        pass

    classes = [TestClass1, TestClass2]

    mock_class_repository = create_mock_class_repository(classes)

    result = mock_class_repository.get_all()

    assert result == classes


def test_create_diagram():
    class TestClass1:
        pass

    class TestClass2:
        pass

    mock_uml_class1 = UMLClass("TestClass1", [], [])
    mock_uml_class2 = UMLClass("TestClass2", [], [])

    return_mapping = {
        TestClass1: mock_uml_class1,
        TestClass2: mock_uml_class2,
    }
    mock_uml_class_factory = create_mock_uml_class_factory(return_mapping)
    mock_class_repository = create_mock_class_repository([TestClass1, TestClass2])

    diagram_factory = DiagramFactory(mock_uml_class_factory, mock_class_repository)

    result = diagram_factory.create_diagram()

    expected_result = UMLDiagram(frozenset([mock_uml_class1, mock_uml_class2]))

    assert result == expected_result
