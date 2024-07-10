import random

lista = ["Siemaneczko", "Brzęszczyczykiewicz", "Mercedes", "Gruszka"]
slowo = random.choice(lista)
rand = ''.join(random.sample(slowo, len(slowo)))
print('Witaj w "Odgadnij Słowo" :D\nJeśli chcesz przerwać grę wpisz "q" lub "Q"')
shot = input(f"Zgadnij co to za słowo: {rand}\n")
while shot != slowo:
        if shot == "q" or shot == "Q":
                break
        shot = input("Spróbuj jeszcze raz: ")
if shot == "q" or shot == "Q":
    print("Przerwano grę")
else:
    print("Brawo, odgadłeś słowo :D")