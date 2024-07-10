b = 1
szer = 64
print("-" * szer)
print("   |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |")
for i in range(1, 11):
    print("-" * szer)
    if (i)>=10:
        print(i,"|  ", end="")
    else:
        print(i," |  ", end="")
    for i in range (1,11):
        print(i*b, end="")
        if (i*b)>=10:
            print(" |  ", end="")
        else:
            print("  |  ", end="")
    print()
    b=b+1
print("-" * szer)