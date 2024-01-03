# Introductions exercises
import math
from math import sin, cos, acos
from math import radians, pi, sqrt
import time
from time import asctime

# 1 Mail

print("Please tell us your name")
name = input()
print("This would be your mail", name + "@gmail.com")

# 2 Hello
Name = str(input((print('Please tell us ur name'))))

print('Hello', Name)

# Area of the room

w = float(input(print('Please enter the width')))
L = float(input(print('Please enter the length')))

area = w * L / 2
print('The area is', area, 'square meters')

# Area of the field

wigth = float(input(print('Please enter the width')))
Length = float(input(print('Please enter the length')))

Area = wigth * Length / 2
acre = Area * 43.560

print('the area is ', Area, 'square meters, but in acres is', acre)

# bottle deposits
one_less = float(input(print('how many bottles did u want')))
one_more = float(input(print('how many bottles of more than a little')))

one_less_counter = 0.10 * one_less
one_more_counter = 0.25 * one_more

print('you need to pay', one_less_counter, '$ for this deposist and for the bottles haves more than a little',
      one_more_counter, '$')

# Tax and tip
print('select the meal: one, two, three')
one = 5.55
two = 20
three = 12.5
print('For one the tax is', one, 'and the tips is', one * 0.18)

# 7 Sum of the forts n positive
n = int(input("enter the int"))
sm = n * (n + 1) / 2
print(int(sm))

# 9 interest
deposits = float(input(print('inter your amount')))
interest_per_years = deposits * 0.04 * 365

print('in one year u will have $%.2f.' % interest_per_years, 'in 2 years will be $%.2f.' % interest_per_years * 2)

# 12 Distance between 2 points

t1 = float(input(print('enter the first one')))
radians(t1)
t2 = float(input(print('enter the seconds')))
radians(t2)
g1 = float(input(print('enter the first one')))
radians(g1)
g2 = float(input(print('enter the seconds ')))
radians(g2)
distance: float = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))
print("the distance is %.2f" % distance)

# 14 Height units
foot = float(input(print('enter')))
inches = foot * 12
cent = inches * 2.54
print('you have %.2f' % foot, 'but the equivalent in inches is %.2f' % inches, 'in centimeters %.2f' % cent)

# Area and volume

radius = float(input('enter'))
area_circle = pi * radius ** 2
volumen = 4 * pi * radius ** 3 / 3

print(area_circle, volumen)

# Free fall
d = float(input('enter the distance'))

vf = sqrt(2 * 9.8 * d)

print('%.2f' % vf)

# 25
days_seconds = 86400
hour_secomds = 3600
min_seconds = 60

seconds = int(input('enter '))
days = seconds / days_seconds
seconds = seconds % days_seconds

hours = seconds / hour_secomds
seconds = seconds / hour_secomds

minutes = seconds / min_seconds
seconds = seconds % min_seconds

print('%d:%02d:%02d:%02d.' % (days, hours, minutes, seconds))

# time.asctime()

# 31 sum of the Digits

number = str(input('enter'))
convert = int(number[0]) + int(number[1]) + int(number[2]) + int(number[3])

# 32 sort 3 number

print('enter 3 interegers')
a = int(input())
b = int(input())
c = int(input())

d = min(a, b, c)
e = max(a, b, c)
f = a + b + c - d - e
print(d, f, e)

# 33 day old bread

