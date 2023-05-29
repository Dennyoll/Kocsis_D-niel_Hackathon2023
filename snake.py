import random

x = random.randint(1,58)

y = random.randint(1,29)

while True:

    if y != 0 and y != 30:
        print("............................................................")
        for i in range(y-1):
            print(".                                                          .")
        if x == 0:
            print("@                                                          .")
        elif x == 59:
            print(".                                                          @")
        elif x != 0:
            print(".",end="")
            for i in range(x-1):
                print(" ",end="")
            print("@",end="")
            for i in range(58-x):
                print(" ",end="")
            print(".")
        for i in range(29-y):
            print(".                                                          .")
        print("............................................................")
    
    elif y == 0:
        for i in range(x):
            print(".",end="")
        print("@",end="")
        for i in range(59-x):
            print(".",end="")
        print("")
        for i in range(28):
            print(".                                                          .")
        print("............................................................")
    
    elif y == 30:
        print("............................................................")
        for i in range(28):
            print(".                                                          .")
        print(".",end="")
        for i in range(x-1):
            print(".",end="")
        print("@",end="")
        for i in range(59-x):
            print(".",end="")
        print("")
    

    print("Hova?")
    if y == 0 or y == 30 or x == 0 or x == 59:
        print("Most ennyi volt, szép napot!")
        break
    else:
        irany = input("")
    


    if irany == "jobbra":
        x = x + 1
    elif irany == "balra":
        x = x - 1
    elif irany == "le":
        y = y + 1
    elif irany == "fel":
        y = y - 1
    elif irany == "meguntam":
        print("Most ennyi volt, szép napot!")
        break