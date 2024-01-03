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

# Morse Code Translate
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

# Postal Codes
