
class ClassRepository:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ClassRepository, cls).__new__(cls)
            cls._instance.__init__()
        return cls._instance
    def __init__(self):
        self.classes = []

    def add(self, cls):
        self.classes.append(cls)


    def get_all(self):
        return self.classes
