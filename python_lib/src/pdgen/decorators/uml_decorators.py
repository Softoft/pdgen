import inspect
import logging

from pdgen.repositories.class_repository import ClassRepository

logger = logging.getLogger("pdgen")

def include_in_uml(target):
    logger.debug("Adding to UML: %s", target)
    if inspect.isclass(target):
        ClassRepository.get_instance().add(target)
        return target
    if inspect.isfunction(target) or inspect.ismethod(target):
        def wrapper(*args, **kwargs):
            return target(*args, **kwargs)

        wrapper.__is_uml_method__ = True
        return wrapper
    raise TypeError(f"The {include_in_uml.__name__} decorator "
                    "can only be applied to classes or methods.")
