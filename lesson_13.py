# Клас повинен підтримувати всі методи батьківського класу, а також:
# Площа кола та довжина кола.

import math
from task_01 import Point


class Circle(Point):

    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f'Circle(x={self.x}, y={self.y}, radius={self.radius})'

    def __add__(self, other):
        new_obj = super().__add__(other)
        return Circle(new_obj.x, new_obj.y, self.radius + other.radius)

    def __sub__(self, other):
        if self.radius == other.radius:
            return Point(self.x, self.y)
        else:
            new_x = self.x - other.x
            new_y = self.y - other.y
            new_radius = abs(self.radius - other.radius)
            return Circle(new_x, new_y, new_radius)


r_1 = Circle()
r_2 = Circle(1, 3, 2)
r_3 = Circle(1, 3, 5)

print(r_1)
print(r_2)
print(r_3)
print(r_3.distance_from_origin())

print(r_3.area())
print(r_3.circumference())

r_new = r_2 + r_3
print(r_new)
r2_new = r_2 - r_3
print(r2_new)
