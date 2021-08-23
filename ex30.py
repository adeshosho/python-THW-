people = 30
cars = 40
trucks = 15


if cars > people: # si hay mas carros que personas
    print("We should take the cars.")
elif cars < people: # o si hay menos carros que personas
    print("We should not take the cars.")
else: # si no cumple con ninguna de las condiciones anteriores
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")