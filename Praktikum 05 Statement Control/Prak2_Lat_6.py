print('"Hai..nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!"')
from random import randint
poin = 0
while True:
    angka = int(input('Tebakan Anda:'))
    bil = randint(0,100)
    if (angka < 20):
        print('Hehehe...Bilangan tebakan anda terlalu kecil')
        poin +=2
    elif (angka > 20):
        print('Hehehe...Bilangan tebakan anda terlalu besar')
        poin +=2
    elif (angka == 20):
        print('Yeeee... Bilangan tebakan anda BENAR:-)')
        score = 100 - poin
        print('Score Anda:' + str(score))
        break
