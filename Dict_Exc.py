# Dictionary EXC
import random
import string


# 128 Reverse Lookup


def reverse_lookup(dicts, value):
    list_key = []
    for k in dicts():
        if dicts[k] == value:
            list_key.append(k)
            return list_key


dicts = {}
reverse_lookup(dicts, '')
print(reverse_lookup(dicts))

# 129 Two dice roller

num_runs = 1000
dice_max = 6


def twice():
    d1 = random.randrange(1, dice_max + 1)
    d2 = random.randrange(1, dice_max + 1)
    return d1 + d2


expect = {2: 1 / 36, 3: 2 / 36, 4: 3 / 36, 5: 4 / 36, 6: 5 / 36, 7: 6 / 36, 8: 5 / 36,
          9: 4 / 36, 10: 3 / 36, 11: 2 / 36, 12: 1 / 36}
count = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0,
         9: 0, 10: 0, 11: 0, 12: 0}

for i in range(num_runs):
    t = twice()
    count[t] = count[t] + 1

for i in sorted(count.keys()):
    print('%5d, %11.2f, %8.2f' % (i, count[i] / num_runs * 100, expect[i] * 100))

# 130 Texting massages
tex_mex = {'1': ['.', ',', '?', '!'],
           '2': ['A', 'B', 'C'],
           '3': ['D', 'E', 'F'],
           '4': ['G', 'H', 'I'],
           '5': ['J', 'K', 'L'],
           '6': ['M', 'N', 'O'],
           '7': ['P', 'Q', 'R', 'S'],
           '8': ['T', 'U', 'V'],
           '9': ['W', 'X', 'Y', 'Z'],
           '0': [' ']}


def texting(mess):
    mess = mess.upper()
    key_press = ''
    for char in mess:
        for k, lista in tex_mex.items():
            if char in lista:
                key_press += k * (lista.index(char) + 1)
    return key_press


mes = str(input('enter a sentences'))
key_pres = texting(mes)
print(key_pres)

# 131 Morse Code Translate
morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
              'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
              'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


def morse_translate(texts):
    text = texts.translate(str.maketrans("", "", string.punctuation))
    text_1 = text.replace(" ", "").upper()
    morse_text = ''
    for element in text_1:
        for k, v in morse_code.items():
            if element in k:
                morse_text += v
    return morse_text


traducir = input('di una frase')
morse_text = morse_translate(traducir)
print(morse_text)


# 132 Postal Codes muy pesado
# 133 Number in english


def number_to_words(number):
    # Define dictionaries for mapping digits and teens
    digits = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }

    teens = {
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
        18: 'eighteen', 19: 'nineteen'
    }

    tens = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
    }

    # Handle special cases for 0-19
    if number < 20:
        if number < 10:
            return digits[number]
        else:
            return teens[number]

    # Handle numbers between 20 and 99
    if number < 100:
        tens_digit = number // 10
        ones_digit = number % 10
        if ones_digit == 0:
            return tens[tens_digit]
        else:
            return tens[tens_digit] + ' ' + digits[ones_digit]

    # Handle numbers between 100 and 999
    hundreds_digit = number // 100
    tens_digit = (number // 10) % 10
    ones_digit = number % 10

    # Build the English words for the number
    words = digits[hundreds_digit] + ' hundred'
    if tens_digit == 0 and ones_digit == 0:
        return words
    else:
        words += ' and '
        if tens_digit == 0:
            words += digits[ones_digit]
        elif tens_digit == 1:
            words += teens[tens_digit * 10 + ones_digit]
        else:
            words += tens[tens_digit]
            if ones_digit != 0:
                words += ' ' + digits[ones_digit]

    return words


num = int(input('Enter a number between 0 and 999: '))
word = number_to_words(num)
print(word)


# 134 unique Character


def unique(s):
    character = {}
    for ch in s:
        character[ch] = True
    return character


string = input('enter a text')
strings = unique(string)
print('the numbers of unique character is', len(strings))


# 135 Anagrams


def anagrams(seq1, seq2):
    if len(seq1) == len(seq2):
        is_anagrams = dict(zip(seq1, seq2))
        for k, v in is_anagrams.items():
            if k[:] == v[::-1]:
                return True
            else:
                return False
    else:
        print('cannot be anagrams they not have the same len')


seq_1 = [input('enter a word')]
seq_2 = [input('enter a second word')]

anagrams(seq_1, seq_2)


# 136 Anagrams Again


def anagrams_generalize(phrase1, phrase2):
    text_1 = phrase1.translate(str.maketrans("", "", string.punctuation))
    text1 = text_1.replace(" ", "").lower()

    text_2 = phrase2.translate(str.maketrans("", "", string.punctuation))
    text2 = text_2.replace(" ", "").lower()

    text2 = sorted(text2)
    text1 = sorted(text1)

    return text1 == text2


l1 = input('enter')
l2 = input('2 enter')

if anagrams_generalize(l1, l2):
    print("Las frases son anagrams.")
else:
    print("Las frases no son anagrams.")

# 137 Scrabble Scores Duda

scrabble_table = {1: ['A', 'E', 'I', 'T', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
                  2: ['D', 'G'],
                  3: ['B', 'C', 'M', 'P'],
                  4: ['F', 'H', 'V', 'W', 'Y'],
                  5: 'K',
                  8: ['J', 'X'],
                  10: ['Q', 'Z']}
values_list = []


def scrabble_predictions():
    counter = 4
    total_point = 0
    while counter > len(values_list):
        letter = str(input("enter a vocals "))
        letter = letter.upper()
        values_list.append(letter)
        letter = str(input("enter a vocals "))
        if letter == '':
            break
    for element in values_list:
        for k, v in scrabble_table.items():
            if element in v:
                total_point += k

    return total_point

# 138 Bingo Cards
number_per_letter = 15


def create_card():
    card = {}
    lower = 1
    upper = number_per_letter

    for letter in ['B', 'I', 'N', 'G', 'O']:
        card[letter] = []
        while len(card[letter]) != 5:
            next_number = random.randrange(lower, upper)
            if next_number not in card[letter]:
                card[letter].append(next_number)
        lower += number_per_letter
        upper += number_per_letter

    return card


def display_card(card):
    print('B I N G O')
    for o in range(5):
        for letter in ['B', 'I', 'N', 'G', 'O']:
            print('%.2d' % card[letter][o], end=' ')

cards = create_card()

display_card(cards)
