class Student:
    def __init__(self, name, roll):
        self._name = name
        self._roll = roll

    @property
    def info(self):
        print(f"Name: {self._name}, Roll: {self._roll}")

    @info.setter
    def info(self, params):
        self._name = params["name"]
        self._roll = params["roll"]

    @info.deleter
    def info(self):
        self._name = None
        self._roll = None

s = Student("John", 1)
s.info
s.info = {"name": "Jane", "roll": 2}
s.info

s2 = Student("Alice", 3)
s2.info
del s2.info
s2.info