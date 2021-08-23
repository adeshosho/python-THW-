formatter = "{} {} {} {}"


print(formatter.format(1, 2, 3, 4)) #pasa los numeros como parametro
print(formatter.format("one", "two", "three", "four"))# pasa strigs como parametro
print(formatter.format(True, False, False, True))#pasa booleanos como parametro
print(formatter.format(formatter, formatter, formatter, formatter))#pasa la misma variable como parametro
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)) # esta parte lo escribe todo junto