from src.converters.attribute_converter import AttributeConverter
from src.converters.class_converter import ClassConverter
from src.converters.diagram_converter import DiagramConverter
from src.converters.method_converter import MethodConverter
from src.factories.attribute_factory.attribute_factory import AttributeFactory
from src.factories.class_factory.class_factory import ClassFactory
from src.factories.diagram_factory.diagram_factory import DiagramFactory
from src.factories.method_factory.method_factory import MethodFactory
from src.factories.type_hints.type_hint_service import TypeHintService
from src.repositories.class_repository import ClassRepository
from src.uml_generation.plantuml_renderer import PlantUMLRenderer
from src.uml_generation.plantuml_service import PlantUMLService


def get_plant_uml_service():
    class_repo = ClassRepository()

    type_hint_service = TypeHintService()

    attribute_converter = AttributeConverter()
    method_converter = MethodConverter()
    class_converter = ClassConverter(attribute_converter, method_converter)
    diagram_converter = DiagramConverter(class_converter)

    attribute_factory = AttributeFactory(type_hint_service)
    method_factory = MethodFactory(type_hint_service)
    class_factory = ClassFactory(attribute_factory, method_factory)
    diagram_factory = DiagramFactory(class_factory, class_repo)

    plantuml_renderer = PlantUMLRenderer()

    plantuml_service = PlantUMLService(diagram_factory, diagram_converter, plantuml_renderer)

    return plantuml_service
