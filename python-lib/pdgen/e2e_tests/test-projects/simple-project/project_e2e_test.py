from pathlib import Path

from src import include_in_uml, generate_diagram

@include_in_uml
class Vehicle:
    def __init__(self, name: str):
        self.name = name

@include_in_uml
class Car(Vehicle):
    def __init__(self, name: str, make: str, model: str):
        self.make = make
        self.model = model
        super().__init__(name)

    @include_in_uml
    def drive(self):
        pass

    @include_in_uml
    def park(self):
        pass


if __name__ == '__main__':
    generate_diagram(Path("diagram_new.png"), Path("diagram_new.txt"))
