# Files exc
import sys
import random


# 141 Display the head of the file


def head():
    try:
        with open('words.txt', 'r') as file:
            lines = file.readlines()
            for line in lines[:10]:
                print(line, end='')
    except FileNotFoundError:
        print(f'Error: cannot found {file}')
    except IOError:
        print('No se puede leer el archivo')


if len(sys.argv) < 2:
    print("Error: Por favor, proporcione un nombre de archivo como parámetro en la línea de comandos.")
else:
    file = sys.argv[1]


# Display the tales of the fail


def tail():
    try:
        with open('words.txt', 'r') as w:
            lines = w.readlines()
            last_lines = lines[-10:]
            for line in last_lines:
                print(line, end='')
    except FileNotFoundError:
        print(f'Error file not found{w}')
    except IOError:
        print('Cannot open')


# 145 Find the longest word in a file


def find_word():
    element_list = []
    element_lenght = 0
    with open('elements.txt', 'r') as elements:
        for line in elements:
            words = line.split()
            for word in words:
                ''.join(i for i in words if i.isalnum())
                word_lenght = len(word)
                if word_lenght > element_lenght:
                    element_lenght = word_lenght
                    element_list = [word]
                elif element_lenght == word_lenght:
                    element_list.append(word)
    return element_lenght, element_list


# 144 Numbers of lines

def add_numbers():
    with open('elements.txt', 'r') as elements, open('output.txt', 'w') as out:
        numbers_line = 1
        for line in elements:
            modify_line = f'{numbers_line}: {line}'
            out.write(modify_line)
            numbers_line += 1


# 148 sum a list of numbers

#line = float(input('enter a numbers'))
#total = 0

#while line != '':
#    try:
#        num = float(line)
#        total = total + num
#        print(total)
#    except ValueError:
#        print(' is would be a number')

#    line = input('enter a number')
#    print('the grand total is', total)


# 150 Remove the comments


def remove_comments():
    with open('List_Exc.py', 'r') as List, open('out.txt', 'w') as out:
        for i in List:
            comments_index = i.find('#')
            if comments_index != 1:
                i = i[:comments_index]
            out.write(i)


# 151 two word random password


def generar_contraseña():
    try:
        with open('words.txt', 'r') as archivo:
            palabras = [palabra.strip().capitalize() for palabra in archivo.readlines() if len(palabra.strip()) >= 3]
            contraseña = ''
            while len(contraseña) < 8 or len(contraseña) > 10:
                contraseña = random.choice(palabras) + random.choice(palabras)
            print("Contraseña generada:", contraseña)
    except FileNotFoundError:
        print(f"Error: Archivo '{'words.txt'}' no encontrado.")
    except IOError:
        print("Error: No se puede leer el archivo de palabras.")


# 152 Whats elements
# duda
def chemist(input_file):
    elements = {}
    with open(input_file, 'r') as chemical:
        for line in chemical:
            line = line.strip().split(',')
            proton = int(line[0].strip())
            symbol = line[1].strip()
            name = line[-1].strip()
            elements[name] = {'symbol': {symbol}, 'protons': protons}
        return elements


def search_protons(elements, proton):
    for name, data in elements.items():
        if data['protons'] == proton:
            return name, data['symbol']
        return None, None


def search_by_name_symbol(elements, search_key):
    search_key = search_key.strip().capitalize()
    if search_key in elements:
        return elements[search_key]['protons']
    for name, data in elements.items():
        if data['symbol'] == search_key:
            return data['protons']
    return None

element = chemist('elements.txt')


def main():
    while True:
        user_input = input("Enter an element symbol, name, or number of protons (blank line to exit): ")
        if not user_input:
            break

        if user_input.isdigit():
            protons = int(user_input)
            names, symbols = search_protons(element, protons)
            if names:
                print(f"Symbol: {symbols}, Name: {names}")
            else:
                print("Error: No element found with the given number of protons.")
        else:
            protons = search_by_name_symbol(element, user_input)
            if protons:
                print(f"Number of protons: {protons}")
            else:
                print("Error: No element found with the given name or symbol.")