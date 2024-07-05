l1 = int(input("Podaj pierwszą liczbę: "))
l2 = int(input("Podaj drugą liczbę: "))
l3 = int(input("Podaj trzecią liczbę: "))

if l1>l2:
    if l1>l3:
        if l2>l3:
            print(l1,l2,l3)
        else:
            print(l1,l3,l2)
    else:
        print(l3,l1,l2)
else:
    if l2>l3:
        if l3>l1:
            print(l2,l3,l1)
        else:
            print(l2,l1,l3)
    else:
        print(l3,l2,l1)