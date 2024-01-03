# Loop Ex
import fractions as frac
import random
from random import randrange
import math
import string
from typing import List

# 61 Average

x = float(input('enter a (enter 0 to exit'))
x_total = 0
x_count = 0

if x == 0:
    print('cannot start with 0')
else:
    pass

while x != 0:
    x_total = x_total + x
    x_count = x_count + 1
    x = float(input('enter a number (enter 0 to exit'))
    average = x_total / x_count
    if x == 0:
        print('this is the end %.2f.' % average)
        break
    else:
        continue

# 62 Discount table
old_price = [4.95, 9.95, 14.95, 19.95, 24.95]
discount_offert = 0.6
for element in old_price:
    new_price = element * discount_offert
    discount = element - new_price
    print('%2f.' % new_price, '\t %2f.' % element, '\t %2f.' % discount)

# Convert Celsius to F
celsius_grade = list(range(0, 100, 10))

for grade in celsius_grade:
    print(grade)
    F_grade = grade * frac.Fraction(9, 5) + 32
    print(grade, '\t', F_grade)

# 64 no more pennies

total_prices = 0
pennies = 5
nickles = 0.05

prices = input('enter a prices')
if prices == ' ':
    print('error')
else:
    pass

while prices != ' ':
    total_prices += float(prices)
    prices = input('enter a prices enter a blank space too exits')
round_total = total_prices * 100 / pennies

if round_total < pennies / 2:
    payment = total_prices - round_total / 100
else:
    payment = total_prices + nickles - round_total / 100

print('%.02f' % total_prices, '\t %.02f' % payment)

# 65 permiter of the polygon

perimeter = 0.0

init_x = float(input('enter the coordinate x'))
init_y = float(input('enter the coordinate y'))

next_x = init_x
next_y = init_y

line = input('enter the x coor blank spce to exit')
while line != '':
    x = float(line)
    y = float(input('y'))
    distance: float = math.sqrt((next_x - x) ** 2 + (next_y - y) ** 2)
    perimeter += distance
    next_x = x
    next_y = y
    line = str(input('enter the x coor blank spce to exit'))

distance = math.sqrt((init_x - x) ** 2 + (init_y - y))
perimeter += distance

print('%.02f' % perimeter)

# Admission Price

# Como lo tengo en la libreta esta bien

# 71 Squere root

print('enter a number')
while True:
    x = input('Enter the number:')
    guess = float(x) / 2
    difference = guess * guess - float(x)
    if difference > 10 ** -12:
        guess = float(x) / guess
    else:
        break
print(guess)

# is a palindrome
line = input('')
is_palindrome = True

for i in range(0, len(line) // 2):
    if line[i] != line[len(line) - i - 1]:
        is_palindrome = False
    if is_palindrome:
        print('si')
    else:
        print('no')

# Other way
line = input("")
if line == line[::-1]:
    print("is T")
else:
    print("no")

# 73 multimple word palindromes

line = input('enter the frase')
line_n = line.translate(str.maketrans('', '', string.punctuation))
line_s = line_n.replace(' ', '').lower()
if line_s == line_s[::-1]:
    print(True)
else:
    print(False)

# 74 Multiplication table
Min = 1
Max = 10
# implemetado en el libro
print("   ", end='')
for i in range(Min, Max + 1):
    print('4%d' % i, end='')
print()
for i in range(Min, Max + 1):
    print('4%d' % i, end='')
print()
for j in range(Min, Max + 1):
    print('4%d' % (i * j), end='')
print()
# Otra via
M = []
for _ in range(1, 10):
    M.append([0 for _ in range(1, 11)])
for i in M[len(M) + 1]:
    for j in M[len(M) + 1]:
        if i < j:
            M[i][j] = (i+1) * (j + 1)
# preguntar despues
# 75 Greatest common divisor

m = int(input(''))
n = int(input(''))

d = min(m, n)

while m % d != 0 or n % d != 0:
    d -= 1
print(d)

# 76 Prime factor
n = int(input('enter a integer'))
factor = 2

if n < 2:
    print('the int have to be more than 2')
else:
    pass

while factor <= n:
    if n % factor == 0:
        print('%s is factor' % factor)
        factor += 1
    else:
        factor += 1


# Maximum integer
Num_items = 100
x_max = randrange(1, Num_items + 1)
x_updates = 0
for values in range(1, Num_items):
    current = randrange(1, Num_items + 1)
    if current > x_max:
        current = x_max
        x_updates += 1
        print(current, '<== Update')
    else:
        print(current)
    print('the max value %d' % x_max, '\n, the # of updates was', x_updates)

num_personas = int(input("Ingrese el número de personas: "))
costo_total = 0
contador = 0
edades = []

while contador < num_personas:
    edad = int(input("diga el grupo de edades {}").format(contador + 1))
    edades.append(edad)
    contador += 1
i = 0
while i < len(edades):
    if edades[i] > 3:
        costo_total += 100
    else:
        continue
    i += 1

print("El costo total de los tickets es:", costo_total)