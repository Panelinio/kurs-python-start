wiek = int(input("Podaj swój wiek: "))
if wiek<18:
    print("Nie jesteś pełnoletni - brakuje Ci {} lat".format(18-wiek))
elif 18<=wiek<100:
    print("Jesteś pełnoletni")
else:
    print("200 lat ♫")