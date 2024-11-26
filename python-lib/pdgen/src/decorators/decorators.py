from src.decorators.store import ClassRepository


def uml_class(*args, **kwargs):
    def decorator(cls):
        class_repo = ClassRepository()
        cls.__uml_methods = []
        class_repo.add(cls)
        return cls
    return decorator


def uml_method(method):
    def wrapper(*args, **kwargs):
        return method(*args, **kwargs)
    method.__is_uml_method__ = True
    wrapper.__is_uml_method__ = True
    return wrapper
