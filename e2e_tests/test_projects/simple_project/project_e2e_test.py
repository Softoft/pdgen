import dataclasses
import time

from pdgen import generate_diagram, include_in_uml


@include_in_uml
class Bike:
    def __init__(self, name: str):
        self.name = name


@include_in_uml
@dataclasses.dataclass
class Car:
    _name: str
    _length: float

    def set_name(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

    @include_in_uml
    def drive(self):
        pass

    @include_in_uml
    def get_fuel_level(self) -> float:
        pass

    @include_in_uml
    def _turn_off_lights(self) -> None:
        pass


def test_generate_diagram(tmp_path):
    """
    Test that the `generate_diagram` function creates the expected output files
    and does not take more than 5 seconds.
    """
    output_image = tmp_path / "diagram_test.png"
    output_text = tmp_path / "diagram_test.txt"

    start_time = time.time()
    generate_diagram(output_image, output_text)
    elapsed_time = time.time() - start_time

    assert output_image.exists(), f"Expected {output_image} to be created."
    assert output_text.exists(), f"Expected {output_text} to be created."

    uml_content = output_text.read_text()
    assert "@startuml" in uml_content, "Expected UML content to start with '@startuml'."
    assert "Bike" in uml_content, "Expected 'Bike' class in UML content."
    assert "Car" in uml_content, "Expected 'Car' class in UML content."

    assert "get_name" not in uml_content, "Expected 'get_name' method to be excluded."
    assert "set_name" not in uml_content, "Expected 'set_name' method to be excluded."

    assert elapsed_time <= 5, f"Diagram generation took too long: {elapsed_time:.2f} seconds."

    file_size_kb = output_image.stat().st_size / 1024
    assert 5 <= file_size_kb <= 5 * 1024, (
        f"Image file size out of range: {file_size_kb:.2f} kB. "
        "Expected size between 5 kB and 5 MB."
    )
