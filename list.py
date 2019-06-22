from geomP import *


l1 = [Point(2, 1), Point(1, 2), Point(0, 0)]
l2 = [Point(4, 0), Point(1, 2), Point(3, 1)]


def x(p):
    return p.x


def y(p):
    return p.y



print(l1 == l2)

sortlx = sorted(l1, key=lambda p: p.x)

sortly = sorted(l2, key=lambda p: p.y)

dist = sorted(l2, key=lambda p: p.distance(Point(0, 0)))

print(sortlx)

print(sortly)

print(dist)




