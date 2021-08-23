from sys import argv

script, filename = argv

txt = open(filename) #abre el archivo pasado por el parametro argv

print(f"Here's your file {filename}:") #imprime un srtring copn el nombre del archivo
print(txt.read()) #lee el documento e imprime el contenido del documento

print("Type the filename again:") #pide el nombre del documento a abrir
file_again = input("> ")

txt_again = open(file_again) #asigna a la variable el documento

print(txt_again.read()) #imprime el contenido del nuevo documento