from pathlib import Path

import plantuml


class PlantUMLRenderer:
    def render(self, plantuml_diagram_text, output_image_file_path: Path):
        """
        Generates and saves the UML diagram to a file.
        """
        assert output_image_file_path.suffix == '.png', 'Output file must be a PNG file'
        puml = plantuml.PlantUML(url='http://www.plantuml.com/plantuml/img/')
        raw_image_data = puml.processes(plantuml_diagram_text)
        with open(output_image_file_path, 'wb') as file:
            file.write(raw_image_data)