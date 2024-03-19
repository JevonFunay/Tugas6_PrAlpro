def angkaprima(c):
    if c <= 1:
        return False
    for i in range(2, c):
        if c % i == 0:
            return False
    return True

def prima_terdekat(j):
    for i in range(j -1, 1, -1):
        if angkaprima(i):
            return i
    return
a = int(input("Masukkan Nilai A: "))
prima = prima_terdekat(a)
print(f"Prima terdekat dari {a} adalah {prima}")   
