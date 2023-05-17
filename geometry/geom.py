#!/usr/bin/env python3

import math


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def angle_bad(self):
        if math.fabs(self.x) < 1e-6:
            return math.pi / 2
        else:
            return math.atan(self.y / self.x)

    def angle(self):
        return math.atan2(self.y, self.x)


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def sub(self, other) -> Vector:
        return Vector(other.x - self.x, other.y - self.y)


def cross(a: Vector, b: Vector) -> float:
    return a.x * b.y - a.y * b.x


def ccw(a: Vector, b: Vector) -> bool:
    return cross(a, b) > 0


def ccw_pt(a: Point, b: Point, c: Point) -> bool:
    v1 = b.sub(a)
    v2 = c.sub(b)
    return ccw(v1, v2)


print(ccw(Vector(1, 0), Vector(0, 1)))  # ccw
print(ccw(Vector(0, 1), Vector(1, 0)))  # cw
print(ccw(Vector(0, -1), Vector(1, 0)))  # ccw
print(ccw(Vector(0, 1), Vector(-1, 0)))  # ccw
print(ccw(Vector(1, 1), Vector(2, 2)))  # collinear

print(ccw_pt(Point(0, 0), Point(1, 1), Point(1, 2)))  # ccw
print(ccw_pt(Point(0, 0), Point(1, 1), Point(1, 0)))  # cw

p0 = Point(0, 0)
p1 = Point(1, 1)    # angle = pi / 4
p2 = Point(-1, -1)  # angle = -3 pi / 4

v1 = p1.sub(p0)
v2 = p2.sub(p0)

print(v1.angle_bad())
print(v2.angle_bad())
print(v1.angle())
print(v2.angle())
