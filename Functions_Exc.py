import math
import string
import random
import re


# 81 Compute the Hypotenuse

def hypotenuse(a, b):
    c = math.sqrt((a ** 2 + b ** 2))
    return print('%.2f' % c)


# Taxi fare

def taxi_fare(x):
    if x >= 140:
        plus = 0.25
        fare = 4.00
        total = fare + (x * plus)
    else:
        total = 4.00
    return print('you have to pay: %.2f' % total)


# 83 Shipping Calculator

def shipping_charge(x):
    prize = 10.95 * x
    adds = 2.95
    total_prize = prize * adds
    return print('you will have to pay %.2f' % total_prize)


# 84 Median of three values

def median(a, b, c):
    Min = min(a, b, c)
    Max = max(a, b, c)
    return a + b + c - Min - Max


# 86 The 12 days of Christmas

def Christmas_Verse(x):
    print('On the %s' % x, 'day of Christmas')
    print('my true love sent to me:')
    if x >= 6:
        print('six leons')
    if x >= 5:
        print(' five cats')
    if x >= 4:
        print('four dogs')
    if x >= 3:
        print('Tree french hens')
    if x >= 2:
        print('Two turtles doves')
    if x == 1:
        print('Nothing its a shit')
    else:
        print('A Partridge in a pear tree', end=' ')
        print()


def all_verse():
    for x in range(1, 7):
        Christmas_Verse(x)


# 87 Center a string
def center_str(a, widht):
    new_string = str(a)
    w = str('-' * widht)
    center = w + new_string
    new_center = center.replace('-', ' ')
    return print(new_center, end=' ')


# 88 Is't a valid traingle


def valid(a, b, c):
    Max = max(a, b, c)
    Sum1 = a + b
    Sum2 = a + c
    Sum3 = b + c
    if Sum1 < Max or Sum2 < Max or Sum3 < Max:
        print('is not a triangle')
    else:
        print('its a triangle')


# 89 Capitalize It
def capitalize_str(s):
    for i in range(len(s)):
        # If the current character is 'i' and it's surrounded by spaces, replace it with 'I'
        if s[i] == 'i' and (i == 0 or s[i - 1] == ' ') and (i == len(s) - 1 or s[i + 1] == ' '):
            s = s[:i] + 'I' + s[i + 1:]
            # If the current character is '.', '!', or '?'
            if s[i] in '.!?':
                j = i + 1
                while j < len(s) and s[j] == ' ':
                    j += 1
                if j < len(s):
                    s = s[:j] + s[j].upper() + s[j + 1:]
        return s


# 90 Does a String Represent an Integer

def isint(x):  # book
    x = x.strip()
    if x[0] == '+' or x[0] == '-' and x[1:].isdigit():
        return True
    if x.isdigit():
        return True
    else:
        return False


def isint_1(x):  # mia
    x = str(x).strip()
    for i in range(len(x)):
        if len(x) >= 1:
            x = x.translate(str.maketrans('', '', string.punctuation))
            new_x = x.replace(' ', '')
            if new_x.startswith('+') or new_x.startswith('-') and new_x[i:].isdigit():
                return True
            elif new_x.isdigit():
                return True
        return False


# 91 Operator precedence

def precedence(s):
    for i in range(len(s)):
        if s[i] == '+' or s[i] == '-':
            print(1)
        elif s[i] == '*' or s[i] == '/':
            print(2)
        elif s[i] == '^':
            print(3)
        else:
            print(-1, '\n not a string')


# its prime number
def prime_detector(n):
    factor = 2
    try:
        n = int(n)
    except ValueError:
        print('invalid literal for int() with base 10: %s' % n)
    if n <= 1:
        return False
    else:
        pass
        for i in range(factor, n):
            if n % i == 0:
                return False
            else:
                return True


# 93 Next prime

def next_prime(n):
    prime = n + 1
    if prime_detector(prime):
        return prime
    prime += 1
    return prime


# 94 Random Password

def random_password():  # mio
    min_len = 7
    max_len = 10
    randomlenght = random.randint(min_len, max_len)
    password = ''
    for i in range(randomlenght):
        password += chr(random.randint(33, 126))
        return


def generate_random_password():
    length = random.randint(7, 10)
    password = ""
    for _ in range(length):
        password += chr(random.randint(33, 126))
    return password


# 95 licencia


def generate_plate(a):
    min_len = 6
    max_len = 7
    plate = str(a) * 3
    for values in range(min_len, max_len + 1):
        new_plate = plate + str(random.randint(0, 9))

        if len(new_plate) == 6:
            print('old, %s' % new_plate)
        else:
            print('new, %s' % new_plate)


def generate_license_plate():  # Poe Solutions
    if random.random() < 0.5:
        # Generate an old license plate format (three letters followed by three numbers)
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        numbers = ''.join(random.choices(string.digits, k=3))
        license_plate = f"{letters}{numbers}"
    else:
        # Generate a new license plate format (four numbers followed by three letters)
        numbers = ''.join(random.choices(string.digits, k=4))
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        license_plate = f"{numbers}{letters}"

    return license_plate


# check password


def ch_pas(password):
    patron = r'(?=.*[A - Z])(?=.*[a - z])(?=.*\d)'
    if len(password) >= 8 and re.search(patron, password):
        return True
    else:
        return False


# 97 Good Password

def good_password():
    password = ''
    attempts = 0
    while not ch_pas(password):
        password = generate_random_password()
        attempts += 1

        print('Good password', password)
        print(attempts)


def hex2int(hex_digit):
    hex_digit = hex_digit.upper()

    if hex_digit not in '0123456789ABCDEF':
        raise ValueError("Invalid hexadecimal digit")

    if hex_digit.isdigit():
        return int(hex_digit)
    else:
        return ord(hex_digit) - ord('A') + 10


def int2hex(integer):
    if integer < 0 or integer > 15:
        raise ValueError("Invalid integer")

    if integer < 10:
        return str(integer)
    else:
        return chr(ord('A') + integer - 10)


# 100


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def get_num_days_in_month(month, year):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


# 101 Reduce fracctions


def min_fac(a, b):
    d = min(a, b)
    while a % d != 0 or b % d != 0:
        d -= 1
        return d


def reduce(num, div):
    if num == 0:
        return print(0, 1)
    x = min_fac(num, div)
    return num // x, div // x


def main():
    num = int(input('enter de num'))
    div = int(input('enter the div'))
    (a, d) = reduce(num, div)
    print('%d, %d can be reduce to %d, %d' % (num, div, a, d))
    main()


# 103 Magics day


def is_magic_date(day, month, year):
    two_digits = year % 100
    return day * month == two_digits


def main():
    print("Magic Dates in the 20th Century:")
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, 32):
                if is_magic_date(day, month, year):
                    print(f"{month}/{day}/{year}")
