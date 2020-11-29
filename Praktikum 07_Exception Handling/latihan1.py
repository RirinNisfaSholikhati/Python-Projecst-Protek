#Latihan1Praktikum07_ExceptionHandling
try:
    nama = input('Masukkan Nama File:')
    print('Isi file', nama,'adalah:')
    file = open(nama, "r")
    print(file.read())
except FileNotFoundError:
    print('File',nama,'tidak ditemukan')
