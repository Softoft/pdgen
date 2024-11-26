from src.store import ALL_CLASSES
from src.uml_types import UMLClass


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
    method.__is_uml_method__ = True
    wrapper.__is_uml_method__ = True
    print(method.__name__)
    print(method.__is_uml_method__)
    return wrapper
