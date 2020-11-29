#Latihan2Praktikum07_ExceptionHandling
try:
    nama = input('Masukkan Nama File:')
    data = input('Data yang mau ditambahkan:')
    file = open(nama, "a")
    file.write(data)
    file.close()
except FileNotFoundError:
    print('File tidak ditemukan')
while True:
    tambah = str(input('Mau lagi (y/n):'))
    if (tambah == 'y') :
        data = input('Data yang mau ditambahkan:')
        file = open(nama, "a")
        file.write(data)
        file.close()
    if (tambah == 'n'):
        break

    

