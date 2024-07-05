seriale = {"Arcane" : 9 , "ATLA" : 10, "Rick and Morty" : 8}
print("Cześć :D Jaki chcesz serial obejrzeć?\n", list(seriale.keys()))
serial = input()
print("Ocena",serial,"to",seriale[serial])
new = input("Teraz podaj swój serial \n")
ocena = input("W skali od 1 do 10 na ile go oceniasz? \n")
seriale = {"Arcane" : 9 , "ATLA" : 10, "Rick and Morty" : 8, new : ocena}
print(seriale)