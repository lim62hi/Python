from typing import Any


class Point:
    'The class for points'
    min = 0
    def __init__(self, x = None, y = None, *args):
        self.set(x, y)
        print(f'Information about new object at {self}: x = {x}, y = {y}')
    def __del__(self):
        info = tuple(self.get().values())
        print(f'Delete object at {self}. Information: x = {info[0]}, y = {info[1]}')
    def __delattr__(self, item):
        print('An attribute was successfully deleted!')
        object.__delattr__(self, item)
    def __getattribute__(self, item):
        print('An attribute was successfully gotten!')
        object.__getattribute__(self, item)
    def __getattr__(self, item):
        return None
    def __setattr__(self, name, value):
        print('An attribute was successfully setted!')
        object.__setattr__(name, value)
    @staticmethod
    def __check(num):
        return type(num) in (int, float)
    def set(self, x, y):
        if self.__check(x) or self.__check(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Irregular numbers!')
    def get(self):
        return {'x': self.__x, 'y': self.__y}
    @classmethod
    def min_class(cls, other):
        cls.min = other
first = Point(2, 3).min_class(5)






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
    @staticmethod
    def connect():
        print(f'DataBase connected')
    @staticmethod
    def write(data = None):
        if data != None:
            print(f'{data} was been written to database')
        else:
            return None
    def read(self):
        print(f'Info: {self.user}, {self.psw}')
    @staticmethod
    def close():
        print('Database closed')