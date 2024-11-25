import inspect
import json

from src import uml_class, uml_method, generate_diagram

@uml_class()
class Vehicle:
    def __init__(self, name: str):
        self.name = name

@uml_class()
class Car(Vehicle):
    def __init__(self, name: str, make: str, model: str):
        self.make = make
        self.model = model
        super().__init__(name)

    @uml_method
    def drive(self):
        pass

    @uml_method
    def park(self):
        pass


if __name__ == '__main__':
    generate_diagram()

    print(Car.park.__hash__())




