import logging
from pathlib import Path

from pdgen.converters.diagram_converter import DiagramConverter
from pdgen.factories.diagram_factory.diagram_factory import DiagramFactory
from pdgen.uml_generation.plantuml_renderer import PlantUMLRenderer
from pdgen.uml_types.types import UMLDiagram


class PlantUMLService:
    """
    Service class for generating UML diagrams using PlantUML.

    Attributes:
        _diagram_factory (DiagramFactory): Factory for creating UML diagrams.
        _plantuml_converter (DiagramConverter): Converter: transforming Diagram Object to PlantUML
        _plantuml_renderer (PlantUMLRenderer): Renderer: generating image files from PlantUML
        _logger (logging.Logger): Logger for logging information and errors.
    """

    def __init__(self,
                 diagram_factory: DiagramFactory,
                 diagram_converter: DiagramConverter,
                 plantuml_renderer: PlantUMLRenderer
                 ):
        self._diagram_factory: DiagramFactory = diagram_factory
        self._plantuml_converter: DiagramConverter = diagram_converter
        self._plantuml_renderer: PlantUMLRenderer = plantuml_renderer
        self._logger = logging.getLogger("pdgen")

    def generate_diagram(self,
                         output_image_file_path: str | Path | None = None,
                         output_text_file_path: str | Path | None = None
                         ):
        """
        Generates a UML diagram and saves it to a file.
        Args:
            output_image_file_path:  Path to the output image file.
            output_text_file_path:  Path to the output text file.

        Returns:
            None
        """
        if output_image_file_path is None and output_text_file_path is None:
            raise ValueError("At least one of output_image_file_path or output_text_file_path must be provided.")

        self._logger.info("Creating UML Diagram ...")
        plantuml_diagram_text = self.generate_plantuml_diagram_text()
        if output_image_file_path is not None:
            self._plantuml_renderer.render(plantuml_diagram_text, output_image_file_path)
        if output_text_file_path is not None:
            self._write_plantuml_text(plantuml_diagram_text, output_text_file_path)

    def generate_plantuml_diagram_text(self) -> str:
        """
        Generates a UML diagram and returns the PlantUML text.
        Returns:
            str: PlantUML text representing the UML diagram.
        """
        plantuml_diagram: UMLDiagram = self._diagram_factory.create_diagram()
        self._logger.info("Creating UML Diagram ...")
        return self._plantuml_converter.convert(plantuml_diagram)

    def _write_plantuml_text(self, plantuml_text: str, output_text_file_path: str | Path):
        with open(output_text_file_path, 'w', encoding="utf-8") as file:
            file.write(plantuml_text)
