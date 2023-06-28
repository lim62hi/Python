class cat:
    name = None
    age = None
    happy = None
    def __init__(self, name = None, age = None, happy = None):
        self.set(name, age, happy)
        print(self.info())

    def set(self, name = None, age = None, happy = None):
        self.name = name
        self.age = age
        self.happy = happy
    
    def info(self):
        return f'Информация про кота с кличкой "{self.name}": возраст: {self.age}; счастлив: {self.happy}'

cat1 = cat('Мурзик', 2)
cat2 = cat('Барсик', 6, False)
