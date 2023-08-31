class Person:
    __instance = None
    def __new__(cls, *args):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, age = None, name = None):
        self.set(age, name)
    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True
        else:
            return False
    def get(self):
        return {'age': self.age, 'name': self.name, 'is_adult': self.adult}
    def set(self, age = None, name = None):
        self.age = age
        self.name = name
        if age != None:
            self.adult = self.is_adult(age)
man = Person(5, 'lim')
print(man.get())