#P08_PythonProject_12

HargaBuah = {'apel' : 5000,
             'jeruk' : 8500,
             'mangga' : 7800,
             'duku' : 6500}
data = list(HargaBuah)
print('Menu:')
print('A. Tambah data buah')
print('B. Beli buah')
print('C. Hapus data buah')
print('D. Selesai')

while True:
    print()
    jawab = str(input('Pilihan menu :'))
    if (jawab == 'A'):
        try:
            key = str(input('Masukkan nama buah:'))
            values = int(input('Masukkan harga satuan:'))
            HargaBuah[key]=values
            print('Data buah :\n')
            for x,y in HargaBuah.items():
                print('-',x,'(','Harga Rp',y,')')
            print()
        except ValueError:
            print('Input tidak valid')
        
    if(jawab == 'B'):
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

    if (jawab == 'C'):
        try:
            nama = str(input('Masukkan nama buah yang ingin dihapus:'))
            del HargaBuah[nama]
            for x,y in HargaBuah.items():
                print('-',x,'(','Harga Rp',y,')')
        except KeyError:
            print('Nama buah tidak ada')
    if (jawab == 'D'):
        break
        
            
                 
              
