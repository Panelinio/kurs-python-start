import random

rand = random.randint(1, 30)
print(rand)
shot = int(input("Zgadnij liczbę od 1 do 30: "))
while shot != rand:
    if shot>rand:
        print("Podałeś za dużą liczbę")
    elif shot<rand:
        print("Podałeś za małą liczbę")
    shot = int(input("Spróbuj jeszcze raz: "))
print("Brawo, udało Ci się zgadnąć liczbę :D")