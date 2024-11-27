import inspect


class ClassRepository:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ClassRepository, cls).__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        self._classes = []

    def add(self, cls: type):
        """
        Add a class to the repository. Only classes can be added, and built-in types are not allowed.
        """
        print(f"Added to CLass Repo: " + cls.__name__)
        if not inspect.isclass(cls):
            raise ValueError("Only classes can be added to the repository.")
        if cls.__module__ == "builtins":
            raise ValueError("Built-in types cannot be added to the repository.")
        self._classes.append(cls)

    def get_all(self):
        return self._classes

    def clear(self):
        self._classes = []

    def __contains__(self, item):
        return item in self._classes
