import inspect
from src.services.uml_class_repository import UMLClassRepository

class_repo = UMLClassRepository()

def get_all_functions(cls):
    return inspect.getmembers(cls, lambda x: inspect.isfunction(x) or inspect.ismethod(x))

def include_in_uml(target):
    if inspect.isclass(target):
        class_repo.add(target)
        return target
    elif inspect.isfunction(target) or inspect.ismethod(target):
        def wrapper(*args, **kwargs):
            return target(*args, **kwargs)
        wrapper.__is_uml_method__ = True
        return wrapper
    else:
        raise TypeError("The include_in_uml decorator can only be applied to _classes or methods.")
