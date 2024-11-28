import logging
from pathlib import Path

from pdgen.converters.diagram_converter import DiagramConverter
from pdgen.factories.diagram_factory.diagram_factory import DiagramFactory
from pdgen.uml_generation.plantuml_renderer import PlantUMLRenderer
from pdgen.uml_types.types import UMLDiagram


class PlantUMLService:
    def __init__(self,
                 diagram_factory: DiagramFactory,
                 diagram_converter: DiagramConverter,
                 plantuml_renderer: PlantUMLRenderer
                 ):

        self._diagram_factory: DiagramFactory = diagram_factory
        self._plantuml_converter: DiagramConverter = diagram_converter
        self._plantuml_renderer: PlantUMLRenderer = plantuml_renderer
        self._logger = logging.getLogger("pdgen")

    def generate_diagram(self, output_image_file_path: Path, output_text_file_path: Path):
        plantuml_diagram: UMLDiagram = self._diagram_factory.create_diagram()
        self._logger.info(f"Creating UML Diagram ...")
        plantuml_diagram_text = self._plantuml_converter.convert(plantuml_diagram)
        self._plantuml_renderer.render(plantuml_diagram_text, output_image_file_path)
        self._write_plantuml_text(plantuml_diagram_text, output_text_file_path)

    def _write_plantuml_text(self, plantuml_text: str, output_text_file_path: Path):
        with open(output_text_file_path, 'w') as file:
            file.write(plantuml_text)
