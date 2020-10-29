from random import randint
sum = 0
while True:
    bil = randint(0, 10)
    sum = sum + 1
    print(bil)
    if bil == 5:
        print('Jumlah perulangan:' + str(sum))
        break
