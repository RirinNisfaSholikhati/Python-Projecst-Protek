#P08_PythonProject_10

HargaBuah = {'apel' : 5000,
             'jeruk' : 8500,
             'mangga' : 7800,
             'duku' : 6500}
dataBuah =[]
i = 1

nama = str(input('Nama buah yang dibeli :'))
kg = int(input('Berapa Kg :'))
print()
try:
    harga = HargaBuah[nama]
    TotalHarga = harga*kg
    dataBuah.append(TotalHarga)
    i += 1
except KeyError:
    print('Nama buah tidak ditemukan')

while True:
    tambah = str(input('Beli buah yang lain (y/n)?:'))
    if(tambah == 'y'):
        print()
        nama = str(input('Nama buah yang dibeli :'))
        kg = int(input('Berapa Kg :'))
        print()
    try:
        harga = HargaBuah[nama]
        TotalHarga = harga*kg
        dataBuah.append(TotalHarga)
        i += 1
    except KeyError:
        print('Nama buah tidak ditemukan')
    
    if(tambah == 'n'):
        print('-----------------------------')
        databuah = tuple(dataBuah)
        print('Total Harga :',sum(databuah))
        break
        
