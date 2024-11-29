from pdgen.converters.attribute_converter import AttributeConverter
from pdgen.converters.class_converter import ClassConverter
from pdgen.converters.diagram_converter import DiagramConverter
from pdgen.converters.method_converter import MethodConverter
from pdgen.converters.services.uml_visibility_service import UMLVisibilityService
from pdgen.factories.attribute_factory.attribute_factory import AttributeFactory
from pdgen.factories.class_factory.class_factory import ClassFactory
from pdgen.factories.diagram_factory.diagram_factory import DiagramFactory
from pdgen.factories.method_factory.method_factory import MethodFactory
from pdgen.factories.type_hints.type_hint_service import TypeHintService
from pdgen.repositories.class_repository import ClassRepository
from pdgen.uml_generation.plantuml_renderer import PlantUMLRenderer
from pdgen.uml_generation.plantuml_service import PlantUMLService


def _get_diagram_converter():
    uml_visibility_service = UMLVisibilityService()
    class_converter = ClassConverter(
        AttributeConverter(uml_visibility_service),
        MethodConverter(uml_visibility_service)
    )
    return DiagramConverter(class_converter)


def _get_diagram_factory(class_repository: ClassRepository):
    type_hint_service = TypeHintService()
    class_factory = ClassFactory(
        AttributeFactory(type_hint_service),
        MethodFactory(type_hint_service)
    )
    return DiagramFactory(class_factory, class_repository)


def get_plant_uml_service():
    class_repository = ClassRepository.get_instance()

    diagram_converter = _get_diagram_converter()
    diagram_factory = _get_diagram_factory(class_repository)

    plantuml_renderer = PlantUMLRenderer()

    plantuml_service = PlantUMLService(diagram_factory, diagram_converter, plantuml_renderer)

    return plantuml_service
