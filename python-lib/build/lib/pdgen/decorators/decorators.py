from pdgen.decorators.store import ALL_CLASSES
from pdgen.decorators.uml_types import UMLClass


def uml_class(*args, **kwargs):
    def decorator(cls):
        if not hasattr(cls, '__uml_methods'):
            cls.__uml_methods = []
        uml_class_instance = UMLClass(cls, *args, **kwargs)
        ALL_CLASSES.append(uml_class_instance)
        return cls
    return decorator


def uml_method(method):
    def wrapper(*args, **kwargs):
        return method(*args, **kwargs)

    wrapper._uml_include = True
    if not hasattr(method.__self__, '__uml_methods'):
        method.__self__.__uml_methods = []
    method.__self__.__uml_methods.append(method.__name__)
    return wrapper
