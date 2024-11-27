# PDGen

PDGen is a Python library for generating UML diagrams from Python code using PlantUML. It simplifies UML generation by allowing you to annotate your classes and methods directly in your code, and then generates a UML diagram based on these annotations.

## Features
- **Simple Annotations**: Mark classes and methods to include in your UML diagram using the `@include_in_uml` decorator.
- **PlantUML Integration**: Generates UML diagrams in PlantUML format.
- **Customizable Output**: Save your diagram as an image and optionally output the UML text.

## Installation
Install PDGen via pip:

```bash
pip install pdgen
```

## Quick Start

Here’s how you can use PDGen to generate a UML diagram:

```python
import logging
from pathlib import Path

# Configure logging to see debug output
logging.basicConfig(level=logging.DEBUG)

from pdgen import include_in_uml, generate_diagram

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
    # Generate a UML diagram
    generate_diagram(Path("diagram_new.png"), Path("diagram_new.txt"))
```

### Output
The above script generates:
1. **`diagram_new.png`**: A UML diagram image.
2. **`diagram_new.txt`**: The PlantUML source text for the diagram.

### Example UML Diagram
The generated UML diagram includes the annotated classes and methods:

```
@startuml
skinparam dpi 600

class Vehicle {
    name: str
}

class Car {
    name: str
    model: str
    make: str
    drive()
    park()
}

Vehicle <|-- Car
@enduml
```

## API Reference

### `@include_in_uml`
A decorator used to mark classes or methods for inclusion in the UML diagram.

### `generate_diagram(output_path: Path, uml_text_path: Path)`
Generates a UML diagram and optionally saves the PlantUML source.

- **`output_path`**: Path to save the generated UML diagram (e.g., PNG format).
- **`uml_text_path`**: Path to save the PlantUML source text.

## Logging
PDGen uses Python's `logging` module to output debug information. You can configure the logging level in your script for better insights into the generation process.

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Contributing
Contributions are welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Softoft/pdgen/blob/main/LICENSE) file for details.

## Links
- [Source Code](https://github.com/Softoft/pdgen)
- [Bug Reports](https://github.com/Softoft/pdgen/issues)