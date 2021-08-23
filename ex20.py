from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read()) # abre el archivo para lectura

def rewind(f):
    f.seek(0) #regresa a la posicion 0

def print_a_line(line_count, f): # parametros de linea a imprimir y archivo
    print(line_count, f.readline())

current_file = open(input_file) # abre el archivo

print("First let's print the whole file:\n")

print_all(current_file) # imprime el contenido del archivo

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1 # suma una posicion a la linea de lectura
print_a_line(current_line, current_file)

current_line = current_line + 1 # suma una posicion a la linea de lectura
print_a_line(current_line, current_file)

current_line = current_line + 1 # suma una posicion a la linea de lectura
print_a_line(current_line, current_file)

