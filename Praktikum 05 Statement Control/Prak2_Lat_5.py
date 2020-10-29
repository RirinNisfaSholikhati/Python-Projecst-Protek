print('"Hai..nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!"')
from random import randint
while True:
    angka = int(input('Tebakan Anda:'))
    bil = randint(0,100)
    if (angka < 20):
        print('Hehehe...Bilangan tebakan anda terlalu kecil')
    elif (angka > 20):
        print('Hehehe...Bilangan tebakan anda terlalu besar')
    elif (angka == 20):
        print('Yeeee... Bilangan tebakan anda BENAR:-)')
        break
