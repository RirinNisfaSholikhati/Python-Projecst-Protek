#P10_OperasiFile_4

Nim = input('Masukkan NIM yang mau dicari : ')

file = open("dataOutput2.txt", "r")
files = file.readlines()

for x in range(len(files)):
    if(Nim in files[x]):
        NIM = 'ada'
        if(NIM == 'ada'):
            y = files[x].split('|')
            print('\nData Mahasiswa')
            print('NIM\t:',y[0])
            print('Nama\t:',y[1])
            print('Alamat\t:',y[2])
        break
    if(Nim not in files[x]):
        NIM = 'tdk ada'
        continue
if(NIM == 'tdk ada'):
    print('Data Mahasiswa tidak ditemukan')
    
    
