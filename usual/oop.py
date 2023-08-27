class Point:
    'The class for points'
    color = None
    circle = None
    x = None
    y = None
    def __init__(self, color = None, circle = None, x = None, y = None):
        self.set(color, circle, x, y)
    def set(self, color = None, circle = None, x = None, y = None):
        self.color, self.circle, self.x, self.y = color, circle, x, y
    def get(self):
        return self.color, self.circle, self.x, self.y
first = Point('red', 2, 1, 2)
second = Point('black', 1, 10, 20)
print(first.get())