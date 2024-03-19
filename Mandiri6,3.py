a = int(input("Tinggi: "))
b = int(input("Lebar: "))
c = 1
for i in range(1,a+1):
    for j in range(1,b+1):
        print(c, end=' ')
        c += 1
    print()
    