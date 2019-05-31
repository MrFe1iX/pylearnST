_author_ = 'Dmitry'

from datetime import date
from geomP import *


a = Point(5, 5)
b = Point(10, 15)

print(a == b)
print(b == Point(10, 15))
print(a.distance(b))











data_in_past = date(2001, 5, 15)


print(data_in_past.year)
print(data_in_past.month)
print(data_in_past.day)
print(data_in_past.weekday())


print(type(data_in_past))
