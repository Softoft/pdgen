from pathlib import Path

from src.converters.diagram_converter import DiagramConverter
from src.factories.diagram_factory.diagram_factory import DiagramFactory
from src.uml_generation.plantuml_renderer import PlantUMLRenderer
from src.uml_types.types import UMLDiagram


class PlantUMLService:
    def __init__(self,
                 diagram_factory: DiagramFactory,
                 diagram_converter: DiagramConverter,
                 plantuml_renderer: PlantUMLRenderer
                 ):

        self._diagram_factory: DiagramFactory = diagram_factory
        self._plantuml_converter: DiagramConverter = diagram_converter
        self._plantuml_renderer: PlantUMLRenderer = plantuml_renderer

    def generate_diagram(self, output_image_file_path: Path, output_text_file_path: Path):
        plantuml_diagram: UMLDiagram = self._diagram_factory.create_diagram()
        print(plantuml_diagram)
        plantuml_diagram_text = self._plantuml_converter.convert(plantuml_diagram)
        self._plantuml_renderer.render(plantuml_diagram_text, output_image_file_path)
        self._write_plantuml_text(plantuml_diagram_text, output_text_file_path)

    def _write_plantuml_text(self, plantuml_text: str, output_text_file_path: Path):
        with open(output_text_file_path, 'w') as file:
            file.write(plantuml_text)
