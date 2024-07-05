print("Witaj w kalkulatorze BMI :D")
waga = float(input("Podaj swoją wagę (kg): "))
wzrost = float(input("Podaj swój wzrost (m): "))
BMI = waga/wzrost**2
print("Twoje BMI wynosi:",BMI)

if (BMI<18.5):
    print("Masz niedowagę :(")
elif (18.5<=BMI<24):
    print("Masz normalną wagę :D")
elif (24<=BMI<26.5):
    print("Masz lekką nadwagę, uważaj")
else:
    print("Masz nadwagę!")
    if (30<=BMI<35):
        print("Otyłość I stopnia!")
    elif (35<=BMI<40):
        print("Otyłość II stopnia!")
    elif(40<=BMI):
        print("Otyłość III stopnia!")