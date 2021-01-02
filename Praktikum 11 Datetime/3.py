#P11_Datetime_03

import datetime
def diffDate(x):
    from datetime import date
    y = x.split('/')
    tgl1 = date(year = int(y[0]), month = int(y[1]), day = int(y[2]))
    tgl2 = date.today()
    selisih = tgl1 - tgl2
    selisih.days
    return
terlambat = str(diffDate('2021/1/2'))

Kode = input('Masukkan Kode Member : ')
file = open("DataPeminjamanBuku.txt", "r")
files = file.readlines()
tglkembali = datetime.date.today()

for x in range(len(files)):
    if(Kode in files[x]):
        KODE = 'ada'
        if(KODE == 'ada'):
            y = files[x].split('|')
            print('\nData Peminjaman Buku')
            print('Kode Member\t\t\t:',y[0])
            print('Nama Member\t\t\t:',y[1])
            print('Judul Buku\t\t\t:',y[2])
            print('Tanggal Mulai Peminjaman\t:',y[3])
            print('Tanggal Maks Peminjaman\t\t:',y[4])
            print('Tanggal Pengembalian\t\t:',tglkembali)
            if terlambat == 'None':
                print('Terlambat\t\t\t: -')
                print('Denda\t\t\t\t: Rp.0')           
            else:
                denda = int(terlambat)*2000
                print('Terlambat\t\t\t: ',terlambat)
                print('Denda\t\t\t\t: Rp.',denda)               
        break
    if(Kode not in files[x]):
        KODE = 'tdk ada'
        continue
if(KODE == 'tdk ada'):
    print('Data Peminjaman Buku tidak ditemukan')
    
