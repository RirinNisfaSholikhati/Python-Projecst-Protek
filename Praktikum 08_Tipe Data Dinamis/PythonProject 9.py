#P08_PythonProject_9

HargaBuah = {'apel' : 5000,
             'jeruk' : 8500,
             'mangga' : 7800,
             'duku' : 6500}
nama = str(input('Nama buah yang dibeli :'))
kg = int(input('Berapa Kg :'))
print('-----------------------------')
harga = HargaBuah[nama]
TotalHarga = harga*kg
print('Total Harga :',TotalHarga)

