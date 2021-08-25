i = 0
numbers = []

def agregando_lista(a):
    num = int(a)
    i= 0
    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
print("Inserta un numero: ")
x = input("<")
agregando_lista(x)
print("The numbers: ")

for num in numbers:
    print(num)