import re

from pdgen import generate_plantuml_diagram_text, include_in_uml
from pdgen.repositories.class_repository import ClassRepository


def test_class_in_uml():
    class Car:
        pass

    ClassRepository.get_instance().clear()
    include_in_uml(Car)
    uml_content = generate_plantuml_diagram_text()
    car_class_matches = re.findall(r"class Car\s?{?", uml_content, re.MULTILINE)
    assert len(car_class_matches) == 1


def test_class_has_attributes():
    class Car:
        name: str
        _year: int

    ClassRepository.get_instance().clear()
    include_in_uml(Car)
    uml_content = generate_plantuml_diagram_text()
    name_attribute_matches = re.findall(r"\s*\+\s?name\s?:\s?str", uml_content, re.MULTILINE)
    assert len(name_attribute_matches) == 1
    year_attribute_matches = re.findall(r"\s*[-#]\s?_?year\s?:\s?int", uml_content, re.MULTILINE)
    assert len(year_attribute_matches) == 1


def test_class_method_signature():
    class Car:
        def add_fuel(self, amount: float, fuel_name: str) -> None:
            pass

    ClassRepository.get_instance().clear()
    include_in_uml(Car)
    include_in_uml(Car.add_fuel)
    uml_content = generate_plantuml_diagram_text()
    name_attribute_matches = re.findall(r"\s*\+\s?name\s?:\s?str", uml_content, re.MULTILINE)
    assert len(name_attribute_matches) == 1
    year_attribute_matches = re.findall(r"\s*[-#]\s?_?year\s?:\s?int", uml_content, re.MULTILINE)
    assert len(year_attribute_matches) == 1
