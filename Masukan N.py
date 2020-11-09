import random
n=int(input('Masukkan Nilai N:'))
for i in range(n):
    while 1:
        n=random.random()
        if n < 0.5:
            break
    print(n)
