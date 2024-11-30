import logging
from pathlib import Path

from pdgen.decorators.uml_decorators import include_in_uml
from pdgen.setup.plant_uml_service_setup import get_plant_uml_service

logger = logging.getLogger("pdgen")

if not logger.hasHandlers():
    logger.addHandler(logging.NullHandler())


def generate_diagram(output_image_file_path: str | Path | None = None,
                     output_text_file_path: str | Path | None = None):
    """
    Generates a UML diagram and saves it to a file.
    Args:
        output_image_file_path:  Path to the output image file.
        output_text_file_path:  Path to the output text file.

    Returns:
        None
    """
    plant_uml_service = get_plant_uml_service()
    plant_uml_service.generate_diagram(output_image_file_path, output_text_file_path)


def generate_plantuml_diagram_text() -> str:
    """
    Generates a UML diagram and returns the PlantUML text.
    Returns:
        str: PlantUML text representing the UML diagram.
    """
    plant_uml_service = get_plant_uml_service()
    return plant_uml_service.generate_plantuml_diagram_text()


__all__ = [include_in_uml.__name__, generate_diagram.__name__, generate_plantuml_diagram_text.__name__]
