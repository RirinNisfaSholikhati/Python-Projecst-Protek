#Praktikum2_P07_ExceptionHandling

try:
 file = open("E:/data.txt", "r")
 bil1 = int(file.readline())
 bil2 = int(file.readline())
 hasil = bil1/bil2
 print(bil1, 'dibagi', bil2, 'sama dengan', hasil)


except FileNotFoundError:
    print('File Tidak Ditemukan')
except ZeroDivisionError:
    print('Tidak boleh pembagian dengan nol')
