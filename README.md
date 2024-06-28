# Python: Start
 Darmowy kurs pythona przygotowany przez Ritę Łyczywek. Kurs można znaleźć na stronie [flynerd.pl](https://www.flynerd.pl/2016/12/python-start.html)

## Lekcje
* [#0 - Start](#0---start)
* [#1 - Konsola](#1---konsola)
* [#2 - Co mi powiesz?](#2---co-mi-powiesz)
* [#3 - Napisy](#3---napisy)
* [#4 - Typy i zmienne](#4---typy-i-zmienne)
* [#5 - Edytujemy napisy](#5---edytujemy-napisy)
* [#6 - Instrukcje warunkowe](#6---instrukcje-warunkowe)
* [#7 - Pętla FOR](#7---pętla-for)

## #0 - Start
Prosty skrypt z printem i inputem :D

## #1 - Konsola
TO PYTHON OD RAZU MOŻE BYĆ KALKULATOREM? :O

`** – znak potęgowania`
`/ – znak dzielenia`
`% – znak dzielenia modulo`

Widocznie w konsoli Python sam dobiera komendy... przynajmniej do tych prostych.
Ale jak jednak wpiszemy komendy to output będzie bez cudzysłowów.

`\n - znak nowej linii`
`\t - dodanie tabulacji`
`\’ - apostrof`
`\” - cudzysłów`
`\\ - ukośnik`

![Konsola](./img/ss1.png)

Można też przypisywać zmienne w konsoli. I mamy też pierwsze zadanie, kalkulator BMI :D

![BMI](./img/ss2.png)

No to mamy pierwsze problemy - nie przetestowałem wpierw potęgowania, co sprawiło mi problemy jak je zaimplementować. I dane źle podałem :/

![BMI2](./img/ss3.png)

Teraz zadanie aby to napisać w jednej linii. Ciekawie.

![BMI3](./img/ss4.png)

Chyba czegoś nie zrozumiałem... Wpisałem zatem:

```python
print("Twoje BMI jest równe:",78/1.78**2)
```

Czas na zadanie 2 - zapotrzebowanie kaloryczne.

![PPM](./img/ss5.png)

Miałem małę problemy z zadaniem tylko dlatego, że wpisywałem 6,25 zamiast 6.25 - nauczka na przyszłość :D

No i zadanie wykonane poprawnie :D Odpowiedź od autorki znajduje się [tutaj](https://github.com/ritaly/python-1-zabawy-w-konsoli/blob/master/Odpowiedzi/2.py). 
Tak samo jak z wpisaniem BMI w jednej linii :D

A, jeszcze dla siebie miałem... no to szybko.

![PPM2](./img/ss6.png)

## #2 - "Co mi powiesz?"
Poznawanie funkcji ("coś ma swoją funkcje – tzn, że spełnia określone zadanie").
* funkcja – to fragment kodu, który wykonuje jakąś sekwencje poleceń. Może przyjmować argumenty.
* argumenty – dane niezbędne do wykonania funkcji

![Funkcje](./img/ss7.png)

![Herbata](./img/ss8.png)

Poznałem również użycie float(input())

![Float](./img/ss9.png)

Po stworzeniu kolejnego pliku .py pokazane jest jak go otworzyć z poziomu konsoli. Potrzebujemy zatem ścieżki:
`C:\Users\kacper.twardowski\dev\kurs-python-start\2\hello2.py`

Aby nastepnie w konsoli wprowadzić:
`python C:\Users\kacper.twardowski\dev\kurs-python-start\2\hello2.py`

lub: 
`python .\dev\kurs-python-start\2\hello2.py` 

(ponieważ w konsoli znajdujemy się w katalogu `C:\Users\kacper.twardowski`)

![Skrypt](./img/ss10.png)

Pora na kolejne zadanie :D
```python
print("Hej! Jak się nazywasz?")
imie = input()
print("Witaj",imie+"!\nIle masz lat?")
wiek = input()
print("Młodo wyglądasz :D\nWiesz jaki jest peron z Harrego Potter'a?")
peron = input()
print("Super :D Ale niestety, mając",wiek,"lat nie możesz wejść na peron",peron)
```
Spróbujemy stworzyć własny kod :D
```python
print("Siemanko :D Jak Cię zwą?")
imie = input()
print("Uszanowanie",imie+"!\nCzy gdybyś miał szansę to czy chciałbyś zostać Wiedźminem?")
odp = input()
print("Moim zdaniem Wiedźmin zwany",imie,"byłby nieposkromionym wojownikiem :D")
```

I teraz jako zadania trzeba przerobić kalkulator bmi i program do obliczenia zapotrzebowanie kalorii :D
```python
print("Witaj w kalkulatorze BMI :D")
waga = float(input("Podaj swoją wagę (kg): "))
wzrost = float(input("Podaj swój wzrost (m): "))
print("Twoje BMI wynosi:",waga/wzrost**2)
```
```python
print("Witaj w programie obliczającym zapotrzebowanie kaloryczne dla mężczyzn uprawiających sport kilka razy w tygodniu :D")
waga = float(input("Podaj swoją wagę (kg): "))
wzrost = float(input("Podaj swoją wagę (cm): "))
wiek = float(input("Podaj swój wiek: "))
print("Twoje zapotrzebowanie kaloryczne wynosi:",((10*waga+6.25*wzrost-5*wiek+5)*1.6))
```
## #3 - Napisy
Zapoznanie się z formatowaniem znaków (float, double, long). Jak się okazuje możemy wybrać do ilu miejsc po przecinku ma się liczba pokazać - interpreter sam klasyfikuje format.

Formatowanie tekstu starym i nowym sposobem:
![Format](./img/ss11.png)

![Format2](./img/ss12.png)


## #4 - Typy i zmienne


## #5 - Edytujemy napisy


## #6 - Instrukcje warunkowe


## #7 - Pętla FOR
