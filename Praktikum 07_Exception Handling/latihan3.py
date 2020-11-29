#Latihan3Praktikum07_ExceptionHandling

print('--------------------------')
print('-PROGRAM HITUNG RATA-RATA-')
print('--------------------------')

dataNilai = []
i = 1
try:
    nilai = int(input('Masukkan bilangan bulat:'))
    dataNilai.append(nilai)
    i += 1
except ValueError:
    print('Bukan bilangan bulat')

while True:
    tambah = str(input('Lagi (y/n):'))
    if(tambah == 'y'):
        try:
            nilai = int(input('Masukkan bilangan bulat:'))
            dataNilai.append(nilai)
            i += 1
        except ValueError:
            print('Bukan bilangan bulat')
    if(tambah == 'n'):
        sum = 0
        for i in range(len(dataNilai)):
            sum += dataNilai[i]
        rerata = sum/len(dataNilai)
        print('Rata - ratanya adalah:',rerata)
        break
