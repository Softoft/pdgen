from pathlib import Path

from pdgen import generate_diagram


def generate_diagram_real_path():
    output_image = Path("resources_tmp/diagram_test.png")
    output_text = Path("resources_tmp/diagram_test.txt")
    generate_diagram(output_image, output_text)


if __name__ == '__main__':
    generate_diagram_real_path()
