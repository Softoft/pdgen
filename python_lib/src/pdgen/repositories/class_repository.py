import inspect
import logging


class ClassRepository:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if ClassRepository._instance is not None:
            raise ValueError("Class Repository is a singleton.")
        self._classes = []
        self._logger = logging.getLogger("pdgen")
        self._logger.debug("Class Repository Initialized")
        ClassRepository._instance = self

    def add(self, cls: type):
        """
        Add a class; Only classes can be added, built-in types aren't allowed
        """
        if not inspect.isclass(cls):
            raise ValueError("Only classes can be added to the repository.")
        if cls.__module__ == "builtins":
            raise ValueError("Built-in types cannot be added to the repository.")
        self._logger.debug("Added to Class Repo: %s", cls.__name__)
        self._classes.append(cls)

    def get_all(self):
        return self._classes

    def clear(self):
        self._logger.warning("Clearing Class Repository")
        self._classes = []

    def __contains__(self, item):
        return item in self._classes
