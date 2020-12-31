#P10_OperasiFile_2

file = open("dataOutput2.txt", "w")
nim = input('Masukkan NIM :')
nama = input('Masukkan Nama Mhs :')
alamat = input('Masukkan Alamat :')

file.write(nim + '|' + nama + '|' + alamat + '\n')

while True:
    print()
    ulang = str(input('Ulangi input lagi (y/n) : '))
    print()
    if (ulang == 'y'):
        nim = input('Masukkan NIM :')
        nama = input('Masukkan Nama Mhs :')
        alamat = input('Masukkan Alamat :')

        file.write(nim + '|' + nama + '|' + alamat + '\n')
        
    if (ulang == 'n'):
        break
        

file.close()

