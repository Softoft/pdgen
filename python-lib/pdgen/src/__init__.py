from src.decorators.uml_decorators import include_in_uml


def generate_diagram(output_image_file_path, output_text_file_path):
    from src.setup.dependency_injection import get_plant_uml_service
    from src.uml_generation.plantuml_service import PlantUMLService
    plant_uml_service = get_plant_uml_service()
    plant_uml_service.generate_diagram(output_image_file_path, output_text_file_path)

__all__ = [include_in_uml, generate_diagram]
