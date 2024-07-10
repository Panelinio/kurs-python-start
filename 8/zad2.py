import random

rand = random.randint(1, 30)
shot = int(input("Zgadnij liczbę od 1 do 30: "))
while shot != rand:
    print("Nie zgadłeś :(")
    shot = int(input("Spróbuj jeszcze raz: "))
print("Brawo, udało Ci się zgadnąć liczbę :D")