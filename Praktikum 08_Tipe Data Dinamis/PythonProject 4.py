#P08_PythonProject_4

data = ['Bayam', 'Kangkung', 'Wortel', 'Selada']
print('Menu:')
print('A Tambah data sayur')
print('B Hapus data sayur')
print('C Tampilkan data sayur')

while True:
    jawab = str(input('Pilihan Anda:'))
    if (jawab == 'A'):
        nama = str(input('Masukkan Nama Sayur:'))
        data.append(nama)
        print(data)
    if (jawab == 'B'):
        try:
            nama = str(input('Nama Sayur yang dihapus:'))
            data.remove(nama)
            print(data)
        except ValueError:
            print('Data tidak ditemukan')
    if (jawab == 'C'):
        print(data)
        break
    
