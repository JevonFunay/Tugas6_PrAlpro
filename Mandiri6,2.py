def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def menurun(n):
    for i in range(n, 0, -1):
        print(faktorial(i), end=" ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


n = int(input("Masukkan nilai n: "))
menurun(n)
