j = int(input("Ile razy program ma się wykonać? : "))
for i in range(1,j):
    if (i%3 ==0)and(i%4 == 0):
        print("Hurra!")
    elif i%4 == 0:
        print("Liczba jest podzielna przez 4")
    elif i%3 ==0:
        print("Liczba jest podzielna przez 3")
    else:
        print("*")