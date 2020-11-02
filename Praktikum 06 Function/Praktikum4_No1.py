def jumlah(a,b):
    hasil = a+b
    
a = 10
b = 20
hasil = a + b
jumlah(a,b)
print(hasil)


def jumlah(a,b):
    global hasil
    hasil = a+b
    
a = 10
b = 20
jumlah(a,b)
print(hasil)
