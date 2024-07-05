imiona = {"Kacper" : "męskie", "Ania" : "żeńskie", "Mariusz" : "męskie", "Zosia" : "żeńskie"}
imie = input("Podaj swoje imię: ")
if imie[-1] =='a':
    plec = "żeńskie"
    print("Jesteś kobietą")
    if imie not in imiona:
        print ("Nie mamy takeigo imienia w bazie - już Cię dodajemy")
        imiona[imie] = plec
        print(list(imiona))
    else:
        print("Już mamy takie imię w bazie :D\n",list(imiona))
else:
    plec = "męskie"
    print("Jesteś mężczyzną")
    if imie not in imiona:
        print ("Nie mamy takeigo imienia w bazie - już Cię dodajemy")
        imiona[imie] = plec
        print(list(imiona))
    else:
        print("Już mamy takie imię w bazie :D\n",list(imiona))