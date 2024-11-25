from src.decorators.store import ALL_CLASSES
from src.decorators.uml_types import UMLClass


def uml_class(*args, **kwargs):
    def decorator(cls):
        cls.__uml_methods = []
        uml_class_instance = UMLClass(cls)
        ALL_CLASSES.append(uml_class_instance)
        return cls
    return decorator


def uml_method(method):
    def wrapper(*args, **kwargs):
        return method(*args, **kwargs)
    print(f"Registering method {method.__name__}")
    print(method)
    if hasattr(method, '__self__'):
        cls = method.__self__.__class__  # Instance method
        print(f"Class: {cls}")
    print(method.__hash__())

    return wrapper
