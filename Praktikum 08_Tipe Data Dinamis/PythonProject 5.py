#P08_PythonProject_5

def kuadrat(bil):
    while True:
        n = int(input('Masukkan banyak bilangan:'))
        break
    Nilai = []
    hasil = []
    i = 0
    while(i<n):
         angka = int(input('Masukkan angka yang diinputkan:'))
         hasil.append(angka)
         perkalian = angka**2
         Nilai.append(perkalian)
         i += 1
    print('bil =',hasil)
    print('hasil =',Nilai)

bil = [1,2,3,4]
hasil = kuadrat(bil)
