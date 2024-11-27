import plantuml


def generate_uml_content():
    print("Not implemented")
    diagram_content = "@startuml\n"
    diagram_content += "skinparam dpi 600\n"
    for uml_class in []:
        uml_class.create_all()
        uml_class.add_all_attributes()
        diagram_content += f'class {uml_class.display_name} {{\n'
        for attr in uml_class.attributes:
            diagram_content += f'    {attr.name} : {attr.attr_type}\n'
        for method in uml_class.methods:
            parameter_list = ", ".join(
                [f"{param}: {p_type.__name__}" for param, p_type in method.parameters.items()])
            diagram_content += f'    {method.name}({parameter_list}) : {method.return_type.__name__}\n'
        diagram_content += '}\n'

    diagram_content += "@enduml"
    return diagram_content


def save_diagram(content, filename='diagram.png'):
    """
    Generates and saves the UML diagram to a file.
    """
    puml = plantuml.PlantUML(url='http://www.plantuml.com/plantuml/img/')
    raw_image_data = puml.processes(content)
    with open(filename, 'wb') as file:
        file.write(raw_image_data)


def save_diagram_to_text(content, filename='diagram.txt'):
    """
    Saves the UML diagram to a text file (.txt).
    """
    with open(filename, 'w') as file:
        file.write(content)


def generate_diagram(output_plantuml_filename: str = None, output_image_filename: str = None):
    """
    Generates a UML diagram from the stored _classes and saves it to a file.
    """
    if not output_plantuml_filename:
        output_plantuml_filename = 'diagram.txt'
    if not output_image_filename:
        output_image_filename = 'diagram.png'
    content = generate_uml_content()
    save_diagram(content, output_image_filename)
    save_diagram_to_text(content, output_plantuml_filename)
