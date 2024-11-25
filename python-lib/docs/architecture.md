# Architecture

## User View

Writes python codes, adds decorators, and runs pdgen to generate UML diagrams.

## System

pdgen will parse the python code

To implement the idea of generating a UML diagram with decorators, you can break the process into the following steps:

Step 1: Create a mechanism to track the decorated classes and methods
You need to define decorators for classes and methods, which will add those classes and methods to a list or dictionary,
where you can track them for inclusion in the UML diagram.

1.1 Class and Method Decorators
ClassToUML: A decorator that will add a class to a list or dictionary for tracking.
MethodToUML: A decorator that will add methods to a list, associating them with the correct class.
1.2 Store the classes and methods
You can use a dictionary to map classes to their methods. This will make it easy to generate the PlantUML file later.

python
Copy code
class_registry = {}

def ClassToUML(cls):

# Add the class to the registry

class_registry[cls] = []
return cls

def MethodToUML(method):

# Add the method to the registry of the class the method belongs to

cls = method.__self__.__class__  # Get the class of the method
if cls in class_registry:
class_registry[cls].append(method.__name__)
return method
Step 2: Map classes to methods
After applying the decorators, class_registry will hold a dictionary where the keys are the class objects, and the
values are lists of methods decorated with MethodToUML.

Example:

python
Copy code

# This class will be added to the class_registry with its methods

@ClassToUML
class MyClass:
@MethodToUML
def method1(self):
pass

    @MethodToUML
    def method2(self):
        pass

At this point, class_registry would look like:

python
Copy code
{
MyClass: ['method1', 'method2']
}
Step 3: Generate PlantUML code
Now that you have all the decorated classes and methods, the next step is to generate the PlantUML file from the
registry.

PlantUML uses a simple syntax for class diagrams, for example:

plantuml
Copy code
@startuml
class MyClass {
+method1()
+method2()
}
@enduml
You can write a function that goes through your class_registry and generates the corresponding PlantUML code for the
class and its methods.

python
Copy code
def generate_puml_file(filename):
with open(filename, 'w') as f:
f.write("@startuml\n")

        # Iterate over the class_registry dictionary
        for cls, methods in class_registry.items():
            f.write(f"class {cls.__name__} {{\n")  # Write the class name
            for method in methods:
                f.write(f"    +{method}()\n")  # Write the method names
            f.write("}\n")
        
        f.write("@enduml\n")

This function will generate the .puml file, which contains the UML class diagram.

Step 4: Convert PlantUML to Image
Once you have the .puml file, you can use an external tool like PlantUML to convert it into an image (e.g., PNG). If you
want to automate this, you can use a Python wrapper for PlantUML, or you can call the PlantUML command-line tool
directly.

For example, using the subprocess module to invoke PlantUML:

python
Copy code
import subprocess

def convert_puml_to_image(puml_file, output_format="png"):
command = f"plantumlt -t{output_format} {puml_file}"
subprocess.run(command, shell=True)
This will generate the UML diagram in the desired image format.

Step 5: Example Usage
python
Copy code

# Decorators and code generation

@ClassToUML
class MyClass:
@MethodToUML
def method1(self):
pass

    @MethodToUML
    def method2(self):
        pass

# Generate the PlantUML file

generate_puml_file("output.puml")

# Convert the PlantUML file to an image

convert_puml_to_image("output.puml", "png")
Summary of Steps:
Track decorated classes and methods: Use decorators (ClassToUML and MethodToUML) to add classes and methods to a
registry.
Map the classes to their methods: Use a dictionary (class_registry) to store the mapping of classes to their decorated
methods.
Generate the PlantUML file: Loop through the dictionary to generate the PlantUML syntax for classes and methods.
Convert the .puml file to an image: Use an external tool (e.g., PlantUML) to convert the .puml file into a PNG or other
image formats.
This approach gives you a flexible system where you can specify which parts of your code to include in the UML diagram
using decorators, and then generate the diagram as a PlantUML file and convert it to an image.