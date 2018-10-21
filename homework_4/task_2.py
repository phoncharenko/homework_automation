class Room:

    def __init__(self, x=100, y=100):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return (self.x * 2) + (self.y * 2)


room_param = Room()
print(room_param.area())
print(room_param.perimeter())
