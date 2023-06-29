class dog:
    age = None
    happy = None
    def __init__(self, age = None, happy = None):
        self.age = age
        self.happy = happy
        print(self.info())
    def info(self):
        return f'age: {self.age}, happy: {self.happy}'
    
class bulldog(dog):
    name = None
    def __init__(self, age = None, happy = None, name = None):
        super(bulldog, self).__init__(age, happy)
        self.name = name
        print(self.info())
    def info(self):
        return f'age: {self.age}, happy: {self.happy}, name: {self.name}'


usualdog = dog(3, True)
bull_dog = bulldog(1, False, 'as')