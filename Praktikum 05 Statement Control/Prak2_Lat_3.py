hitung = 0
sum = 0
for i in range(1, 100, 2):
    print(i)
    hitung = hitung + 1 
    suku = i + 1
    sum = sum + suku
print('Banyaknya bilangan ganjil:' + str(hitung))
print('Jumlah seluruh bilangan:' + str(sum))
