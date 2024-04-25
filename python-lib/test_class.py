import pdgen.diagram as pdgen


@pdgen.uml_class()
class Vehicle:
    def __init__(self, name: str):
        self.name = name


@pdgen.uml_class()
class Car(Vehicle):
    def __init__(self, name: str, make: str, model: str):
        self.make = make
        self.model = model
        super().__init__(name)

    def drive(self):
        pass

    def park(self):
        pass


if __name__ == '__main__':
    pdgen.generate_uml_diagram()
