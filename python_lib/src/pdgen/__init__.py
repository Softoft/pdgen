import logging

from pdgen.decorators.uml_decorators import include_in_uml
from pdgen.setup.plant_uml_service_setup import get_plant_uml_service

logger = logging.getLogger("pdgen")

if not logger.hasHandlers():
    logger.addHandler(logging.NullHandler())


def generate_diagram(output_image_file_path, output_text_file_path):
    plant_uml_service = get_plant_uml_service()
    plant_uml_service.generate_diagram(output_image_file_path, output_text_file_path)


__all__ = [include_in_uml.__name__, generate_diagram.__name__]
