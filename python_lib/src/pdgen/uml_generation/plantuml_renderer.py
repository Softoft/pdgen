import base64
import zlib

import requests


class PlantUMLRenderer:
    """
    Renderer for generating UML diagrams using PlantUML.
    """

    def encode_diagram_text(self, plantuml_diagram_text: str) -> str:
        return base64.urlsafe_b64encode(zlib.compress(plantuml_diagram_text.encode(), 9)).decode()

    def _render_svg(self, encoded_diagram_text: str, output_image_file_path: str):
        response = requests.get(f"https://kroki.io/plantuml/svg/{encoded_diagram_text}")
        with open(output_image_file_path, 'w') as file:
            file.write(response.text)

    def _render_png(self, encoded_diagram_text: str, output_image_file_path: str):
        response = requests.get(f"https://kroki.io/plantuml/png/{encoded_diagram_text}")
        with open(output_image_file_path, 'wb') as file:
            file.write(response.content)

    def render(self, plantuml_diagram_text: str, output_image_file_path: str):
        encoded_diagram_text = self.encode_diagram_text(plantuml_diagram_text)

        if output_image_file_path.endswith('.svg'):
            return self._render_svg(encoded_diagram_text, output_image_file_path)
        if output_image_file_path.endswith('.png'):
            return self._render_png(encoded_diagram_text, output_image_file_path)
        raise ValueError("Output file must be a PNG or SVG file")
