import random

lista = []

szamlalo = 1

x = int(input(""))
for i in range(x):
    y = random.randint(1,100)
    lista.append(y)

for i in lista:
    print(i,end=" ")
while True:

    a = random.randint(1,x)

    b = 0

    for i in lista:
        if szamlalo != a:
            szamlalo = szamlalo + 1
        elif szamlalo == a: 
            b = i
            szamlalo = szamlalo + 1

    szamlalo = 1
    lista = []
    lista.append(b)
    for i in range(x-1):
        y = random.randint(1,100)
        if y == b:
            y = random.randint(1,100)
        lista.append(y)

    for i in lista:
        print(i,end=" ")
    print()