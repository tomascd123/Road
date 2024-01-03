# LIST Exc
import string
import random
import re


# 104 Sorted a list


def list_sorted(*numbers):
    numbers_list = []
    for n in numbers:
        numbers_list.append(n)
        numbers_list.sort()
    return numbers_list


# 105 Reverse order


def reverse_sorted(*numbers):
    new_list = []
    for n in numbers:
        new_list.append(n)
        new_list.sort()
        new_list.reverse()
    return new_list


# 106 Remove outliers


def remover_valores_extremos(valores, n):
    if len(valores) < 4:
        raise ValueError("Se requieren al menos 4 valores")
    # Crear una copia nueva de la lista
    nuevos_valores = valores[:]
    # Ordenar la lista en orden ascendente
    nuevos_valores.sort()
    # Eliminar los n elementos más grandes y los n elementos más pequeños
    nuevos_valores = nuevos_valores[n:-n]
    return nuevos_valores


def main():
    try:
        # Leer una lista de números del usuario
        valores = input("Ingresa una lista de números (separados por espacios): ").split()
        valores = [float(valor) for valor in valores]
        # Eliminar los dos valores más grandes y los dos valores más pequeños
        nuevos_valores = remover_valores_extremos(valores, 2)
        # Mostrar la lista con los valores atípicos eliminados
        print("Lista con los valores atípicos eliminados:", nuevos_valores)
        # Mostrar la lista original
        print("Lista original:", valores)
    except ValueError as e:
        print("Error:", str(e))


# 107 Avoid duplicates


def avoid(a):
    values = []
    a = str(input('Enter a word for exit: enter a blank space'))
    while a != ' ':
        odl = a
        a = str(input('Enter a word for exit: enter a blank space'))
        values.append(a)
    new_values = set(values)
    for value in new_values:
        print(value)


# 108 Negatives zeros and positives


def sorted_order():
    values = []
    n = int(input('Enter a intereger, for exit enter a blank spaces: '))
    while n != ' ':
        old = n
        n = input('Enter a intereger, for exit enter a blank spaces: ')
        values.append(n)
        values.sort()
    values.pop(0)
    return values


# 109 Proper divisor


def divisor(n):
    factor = 1
    values = []
    while factor <= n:
        if n % factor == 0:
            values.append(factor)
        else:
            pass
        factor += 1
    return values


def main():
    try:
        # Read a positive integer from the user
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            raise ValueError("Input must be a positive integer")
        div = divisor(n)
        print(div)
    except ValueError as e:
        print("Error:", str(e))


# 110 Perfect Numbers


def is_perfect(n):
    limit = 1000
    if n > limit:
        raise ValueError('el limite es mil')
    div = divisor(n)
    div.pop()
    if n == sum(div):
        return True
    else:
        return False


# 111 Only the words


def string_list():
    s = input('Enter a strings').split()
    s = [str(element) for element in s]
    srt_list = []
    for element in s:
        if element == str().isalpha():
            srt_list.append(element)
        return srt_list


def extract_words(text):
    # Remove punctuation marks at the edges of words
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Split the text into words
    words = text.split()
    return words


# def main():
#   try:
# Read a string from the user
#        text = input("Enter a string: ")

# Extract words from the string
#        words = extract_words(text)

# Display the list of words
#       print("Words:", words)
#    except ValueError as e:
#        print("Error:", str(e))


# Run the main program only if the solution is not imported into another file
# if __name__ == "__main__":
#    main()

# 112 Below and above the average (duda)


def average(n):
    n = float(input('enter a #, for exit press enter:'))
    below_list = []
    above_list = []
    average_list = []
    while n != ' ':
        average_list.append(n)
        n = input('enter a #, for exit press enter')
        average_list.pop(0)
    for element in average_list:
        sum(average_list)
        if element < sum(average_list):
            below_list.append(element)
            print(below_list)
        else:
            above_list.append(element)
            print(above_list)
        return print(average_list, above_list, below_list)


# 113 Formatting a list:


def form_list(items):
    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return items[0]
    else:
        format_list = ', '.join(items[:-1])
        format_list += ' and ' + items[-1]
        return format_list


def main():
    items = []
    while True:
        item = input('enter a item or a bs to finish')
        if item == ' ':
            break
        items.append(item)
    formatted = form_list(items)
    print(formatted)


# 114 Random lottery number


def random_number():
    lottery = list(set())
    for i in range(6):
        number = random.randrange(1, 50)
        while number in lottery:
            number = random.randrange(1, 50)
        lottery.append(number)
        lottery.sort()

    for j in lottery:
        print(j, end=' ')


# 115


def piglatin(s):
    words = re.findall(r'\b\w+\b', s)
    for i in words:
        words_v = re.search(r'[aeiou]', i, re.IGNORECASE)
        # words_c = re.search(r'[^aeiou]', i, re.IGNORECASE)
        if words_v:
            indice = words_v.start()
            lat_ay = i[:indice + 1] + 'ay' + i[indice + 1:]
            words_v.group()


# 117 Line of best fit


def calculate_line_of_best_fit(points):
    n = len(points)
    sum_x = sum(point[0] for point in points)
    sum_y = sum(point[1] for point in points)
    sum_xy = sum(point[0] * point[1] for point in points)
    sum_x_squared = sum(point[0] ** 2 for point in points)

    x_bar = sum_x / n
    y_bar = sum_y / n

    m = (sum_xy - (n * x_bar * y_bar)) / (sum_x_squared - (n * x_bar ** 2))
    b = y_bar - (m * x_bar)

    return m, b


# Read collection of points from the user
points = []
while True:
    x_input = input("Enter the x-coordinate (blank line to stop): ")
    if x_input == "":
        break
    x = float(x_input)
    y = float(input("Enter the y-coordinate: "))
    points.append((x, y))

# Calculate line of best fit
m, b = calculate_line_of_best_fit(points)

# Display the equation of the line of best fit
equation = f"y = {m}x + {b}"
print("Equation of the line of best fit:", equation)


# Shuffle decks of cards


def create_deck():
    total_cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K']
    shapes = ['h', 's', 'c', 'd']
    all_cards = []
    for i in shapes:
        for j in total_cards:
            all_cards.append(str(j) + i)
            print(all_cards)
            print(len(all_cards))
            return all_cards


def shuffle(cards):
    num_cards = len(cards)
    for i in range(num_cards):
        j = random.randint(i, num_cards - 1)
        cards[i], cards[j] = cards[j], cards[i]
        return cards


def deal(hands, cards_per_hand, deck):
    hands = []
    for _ in range(num_hands):
        hand = []
        for _ in range(cards_per_hand):
            card = deck.pop(0)
            hand.append(card)
        hands.append(hand)

    return hands


# Main program
deck = create_deck()
print("Initial deck:", deck)

shuffled_deck = shuffle(deck)
print("Shuffled deck:", shuffled_deck)

num_hands = 4
cards_per_hand = 5

hands = deal(num_hands, cards_per_hand, shuffled_deck)
print("Hands:")
for i, hand in enumerate(hands):
    print(f"Hand {i + 1}: {hand}")

print("Remaining cards in deck:", shuffled_deck)


# 120 Sort list

def check(*n):
    l = [element for element in n]
    assend = sorted(l)
    dessending = sorted(l, reverse=True)
    if l == assend or l == dessending:
        return True
    else:
        return False


# 121 Count the elements


def counter_range(a, e, c):
    max_value = max(a, e, c)
    min_value = min(a, e, c)
    min_list = []
    for values in range(min_value, max_value + 1):
        if values >= min_value:
            min_list.append(values)
            min_list.count(values)
            return min_list


# 125 Sublist Exc


def is_sublist(lista1, lista2):
    if len(lista1) > len(lista2):
        for element in range(len(lista1) - len(lista2) + 1):
            if lista1[element:element + len(lista2)] == lista2:
                return True
        return False


 # 126 All sublist


def all_sublist(lista_1):
    nested = [[]]
    for element in range(1, len(lista_1) + 1):
        for i in range(0, len(lista_1) - element + 1):
            nested.append(lista_1[i:i + element])
    return nested

lista_1 = [1, 2, 3, 4]
all_sublist(lista_1)


