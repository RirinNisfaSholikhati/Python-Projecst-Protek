#No_1
print('No_1')
a = [1,5,6,9,11,20,12]
b = [7,4,5,6,7,1,12,5,9]
print('List a =',a)
print('List b =',b)
print()

#No_2
print('No_2/Insert')
a.insert(3, 10)
b.insert(2, 15)
print('List a =',a)
print('List b =',b)
print()

#No_3
print('No_3/append')
a.append(4)
b.append(8)
print('List a =',a)
print('List b =',b)
print()

#No_4
print('No_4/Diurutkan secara Ascending')
a.sort()
b.sort()
print('List a =',a)
print('List b =',b)
print()

#No_5
print('No_5/Membuat list c dan d dari sublist a dan b')
c = a[0:8]
d = b[2:10]
print('List c =',c)
print('List d =',d)
print()

#No_6
print('No_6/Menjumlahkan elemen c dan d sesuai indeks')
e = []
for i in range(len(c)):
    elemen = c[i] + d[i]
    e.append(elemen)
print('List e =',e)
print()

#No_7
print('No_7/Mengubah list e ke Tuple')
Tuple_e = tuple(e)
print(Tuple_e)
print()

#No_8
print('No_8/Mencari nilai Min,Max dan Jumlah dari Tuple_e')
print('Nilai Max =',min(Tuple_e))
print('Nilai Max =',max(Tuple_e))
print('Nilai Max =',sum(Tuple_e))
print()

#No_9
print('No_9/Membuat String')
myString = "python adalah bahasa pemrograman yang menyenangkan"
print('Kalimat',myString)
print()

#No_10
print('No_10/Menentukan karakter string dengan menggunakan set')
karakterPenyusun = set(myString)
print('Karakter penyusun string =',karakterPenyusun)
print()

#No_11
print('No_11/Mengurutkan himpunan karater secara alfabet')
Urutan = list(karakterPenyusun)
Urutan.sort()
print('Urutan karakter penyusun string secara Alfabet adalah\n',Urutan)
