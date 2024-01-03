from math import sqrt
import random

# 34 Even or odd

num = int(input('enter a number'))

if num % 2 == 0:
    print('is even')
else:
    print('is odd')

# 35 Dog Tears
human_years = int(input('enter the years'))

first_two = human_years * 5.25
past_two = human_years * 4

if human_years < 0:
    print('is a dog not jesus')
elif human_years <= 2:
    print(human_years * first_two)
else:
    print(human_years * past_two)

# vowel or Consonant
vocals = ['a', 'e', 'i', 'o', 'u']

letter = str(input('input'))

for element in vocals:
    if element == letter:
        print('is a vowal')
    else:
        print('c')

# NAME THAT SHAPE

n = str(input('enter'))
if n == 'enero' or n == 'marzo' or n == 'abril':
    print(31)
elif n == 'junio' or n == 'septimebre':
    print(30)
else:
    print('febrero tiene 28')

# 39 Sound levels

sound = int(input('enter'))

if sound <= 40:
    print('its a quite room')
elif 40 < sound <= 70:
    print('probability its the alamar')
elif sound > 70:
    print('its too loud')

# 40 name of that triangle
print('enter the lengths')
a = int(input())
b = int(input())
c = int(input())

if a == b and a == c:
    print('equilateral')
elif a == b and a != c or b == c and b != a:
    print('its isosceles')
else:
    print('scalene')

# 41 Note to frequency
freq_name = str(input('please enter a frequency note'))
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

note = freq_name[0]
octave = int(freq_name[1])
if note == 'C':
    freq_name = C4
elif note == 'D':
    freq_name = D4
elif note == 'E':
    freq_name = E4

freq = freq_name / 2 ** (4 / octave)
print(freq_name, freq)

# 43 Banknotes
amount = int(input('introduce the amount'))
I1 = 'GW'
I2 = 'TJ'

if amount == 1:
    print(I1)
elif amount == 2:
    print(I2)
else:
    print('no have banknotes')

# 44 dATE To Holday

month = str(input('enter a month '))
day = int(input('enter a day'))

if month == 'January' and day == 1:
    print('Its New years day')
elif month == 'July' and day == 1:
    print('Its Canada day')
elif month == 'December' and day == 25:
    print('Christmas day')
else:
    print('it is not a holiday')

# 46 season
month = str(input('enter a month '))
day = int(input('enter a day'))

if month == 'march' and day < 20:
    print('its winter')
elif month == 'march' and day >= 20 or month == 'april' or month == 'may':
    print('its spring')
elif month == 'june' and day < 21:
    print('winter')
elif month == 'june' and day >= 21 or month == 'july' or month == 'august':
    print('summer')

# 50 root of quadratic function

a = float(input('enter'))
b = float(input('enter'))
c = float(input('enter'))

root = (-b + (sqrt(b ** 2 - 4 * a * c))) / (2 * a)
root_1 = (-b - (sqrt(b ** 2 - 4 * a * c))) / (2 * a)
print(root, root_1)

class_note = input('tell us your note')
class_note = class_note.upper()

if class_note == 'A' and class_note == 'A+':
    if class_note == '-A':
        note = 3.7
        print(note)
    note = 4.0
    print(note)
elif class_note == 'B+' or class_note == 'B':
    note = 3.3
    print(note)
else:
    print('enter a real note')

# 53 Assessing employers

UP = 0.0
AP = 0.4
MP = 0.6

rate = float(input('enter your year rate'))
salary = 2400

if rate == UP:
    salary_amount = salary * UP
elif rate == AP:
    salary_amount = salary * AP
elif rate >= MP:
    salary_amount = salary * rate

if UP < rate < AP or rate == 0.5:
    print('not valid')
else:
    print('this is your salary', salary_amount)

# phone bill
bill_cost = 15.00

minutes = float(input('enter the minutes'))
messengers = float(input('enter the messengers'))

if minutes <= 50 and messengers <= 50:
    print('you pay your bild normally')
elif minutes > 50 and messengers > 50:
    bill_tax = bill_cost + (minutes - 50) * 0.25 + (messengers - 50) * 0.15
    print('you have to pay %2f.', bill_tax)
elif minutes > 50:
    bill_tax = bill_cost + (minutes - 50) * 0.25
    print('you have to pay %2f.', bill_tax)
elif messengers > 50:
    bill_tax = bill_cost + (messengers - 50) * 0.15
    print('you have to pay %2f.', bill_tax)
elif minutes and messengers < 0 or minutes < 0 or messengers < 0:
    print('please nor again')

# 60 Roulette Payouts

X = random.randint(0, 37)
Even = X % 2 == 1
Odd = X % 2 == 0

if X == 37:
    print('the roulette spin is 00')
else:
    print('the roulette spin is %d.' % X)

if X == 37:
    print('pay 00')
    print('green')
else:
    print('pay', X)

if X == Even and 1 <= X <= 9 \
        or X == Odd and 12 <= X <= 18 \
        or X == Even and 19 <= X <= 27 \
        or X == Odd and 30 <= X <= 36:
    print('Pay Red')
elif X == 0 and X == 37:
    pass
else:
    print('pay black')

if X == Odd:
    print('Pay Odd')
else:
    print('pay Even')

if 1 <= X <= 18:
    print(' 1 -18')
else:
    print('19-36')
