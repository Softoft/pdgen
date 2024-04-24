from pdgen.decorators import decorators
from pdgen.decorators import generation


def uml_class(cls):
    """
    Decorator to register a class for UML diagram generation.
    """
    return decorators.uml_class(cls)


def uml_method(method):
    """
    Decorator to register a method for UML diagram generation.
    """
    return decorators.uml_method(method)


def generate_uml_diagram(output_plantuml_filename: str = None, output_image_filename: str = None):
    """
    Generates a UML diagram from the stored classes and saves it to a file.
    """
    generation.generate_diagram(
        output_plantuml_filename=output_plantuml_filename,
        output_image_filename=output_image_filename
    )
