class cat:
    name = None
    age = None
    happy = None
    poroda = None
    def __init__(self, name = None, age = None, happy = None, poroda = None):
        self.set(name, age, happy, poroda)
        print(self.info())

    def set(self, name = None, age = None, happy = None, poroda = None):
        self.name = name
        self.age = age
        self.happy = happy
        self.poroda = poroda
    
    def info(self):
        return f'Информация про кота с кличкой "{self.name}": возраст: {self.age}; счастлив: {self.happy}, порода {self.poroda}'

cat1 = cat('Мурзик', 2, True, 'Мурзиковый')
cat2 = cat('Барсик', 6, False)
