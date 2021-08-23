types_of_people = 10
x = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"


print(x)
print(y)


print(f"I said: {x}") # imprimimos lo que esta en X
print(f"I also said: '{y}'")#imprimimos lo que esta en y

hilarious = False #valor booleano
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious)) #Imprimimos mediante una caracteristica una variable

w = "This is the left side of ..."
e = "a string will a right side."

print(w + e)

