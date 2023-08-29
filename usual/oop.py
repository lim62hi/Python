class Point:
    'The class for points'
    def __new__(cls, *args):
        return super().__new__(cls)
    def __init__(self, color = None, circle = None, x = None, y = None, *args):
        self.set(color, circle, x, y)
        print(f'Information about new object at {self}: color = {color}, circle = {circle}, x = {x}, y = {y}')
    def __del__(self):
        info = self.get()
        print(f'Delete object at {self}. Information: color = {info[0]}, circle = {info[1]}, x = {info[2]}, y = {info[3]}')
    def set(self, color = None, circle = None, x = None, y = None):
        self.color, self.circle, self.x, self.y = color, circle, x, y
    def get(self):
        return self.color, self.circle, self.x, self.y

class DataBase:
    'The class for different databases'
    __instance = None
    def __new__(cls, *args):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, user = None, psw = None):
        self.user = user
        self.psw = psw    
    def __del__(self):
        DataBase.__instance = None
        print('Database closed')
    def connect(self):
        print(f'DataBase connected')
    def write(self, data = None):
        if data != None:
            print(f'{data} was been written to database')
        else:
            return None
    def read(self):
        print(f'Info: {self.user}, {self.psw}')
    def close(self):
        print('Database closed')
#first = Point('red', 2, 1, 2)
#second = Point('black', 1, 10, 20)
db = DataBase('lim', ',bpjy123')
db2 = DataBase('asd', 'asdasdsadas')
db.read()
db2.read()
