#P11_Datetime_02

from datetime import*

file = open("DataPeminjamanBuku.txt", "w")
nim = input('Masukkan Kode Member :')
nama = input('Masukkan Nama Member :')
alamat = input('Masukkan Judul Buku :')
HariPinjam = datetime.date(datetime.now())
HariKembali = HariPinjam + timedelta(days = 7)


file.write(nim + '|' + nama + '|' + alamat + '|' + str(HariPinjam) + '|' + str(HariKembali) + '\n')


while True:
    print()
    ulang = str(input('Ulangi input lagi (y/n) : '))
    print()
    if (ulang == 'y'):
        nim = input('Masukkan Kode Member :')
        nama = input('Masukkan Nama Member :')
        alamat = input('Masukkan Judul Buku :')
        HariPinjam = datetime.date(datetime.now())
        HariKembali = HariPinjam + timedelta(days = 7)
        

        file.write(nim + '|' + nama + '|' + alamat + '|' + str(HariPinjam) + '|' + str(HariKembali) + '\n')
        
    if (ulang == 'n'):
        break
        

file.close()
