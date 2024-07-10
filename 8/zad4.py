print("-"*42)
sil = int(input("(While)Podaj dowolną liczbę całkowitą do 15: "))
wej = sil
for i in range(1,sil):
    sil *= i
print(f"{wej}! =",sil)
print("-"*42)
sil = int(input("(For)Podaj dowolną liczbę całkowitą do 15: "))
wej = sil
i = 1
while i!=wej:
    sil *= i
    i += 1
print(f"{wej}! =",sil)