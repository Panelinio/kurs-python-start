l1 = float(input("Podaj pierwszy bok trójkąta: "))
l2 = float(input("Podaj drugi bok trójkąta: "))
l3 = float(input("Podaj trzeci bok trójkąta: "))

if l1>l2:
    if l1>l3:
        if l2>l3:
            troj = [l1,l2,l3]
        else:
            troj = [l1,l3,l2]
    else:
        troj = [l3,l1,l2]
else:
    if l2>l3:
        if l3>l1:
            troj = [l2,l3,l1]
        else:
           troj = [l2,l1,l3]
    else:
        troj = [l3,l2,l1]

a,b,c = troj[2],troj[1],troj[0]

if (a+b) > c:
    print("Podałeś boki trójkąta")
    a2,b2,c2 = a**2,b**2,c**2
    if (a2+b2)==c2:
        print("Twój trójkąt jest pitagorejski :D")
        if (a%3==0) and (b%4==0) and (c%5==0):
            print("I jest egipski :D")
        else:
            print("Ale nie jest egipski")
    else:
        print("Twój tójkąt nie jest pitagorejski")
else:
    print("Podane przez Ciebie boki nie tworzą trójkąta")
