#!/usr/bin/env python3

class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


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
