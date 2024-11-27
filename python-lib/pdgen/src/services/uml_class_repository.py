class UMLClassRepository:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UMLClassRepository, cls).__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        self._classes = []

    def add(self, cls):
        self._classes.append(cls)

    def get_all(self):
        return self._classes

    def clear(self):
        self._classes = []

    def __contains__(self, item):
        return item in self._classes
