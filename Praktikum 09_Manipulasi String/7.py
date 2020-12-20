#P09_ManipulasiString_7

mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('======================================================================')
print('NIM'.ljust(10),'NAMA MAHASISWA'.ljust(20),'TGL LAHIR'.ljust(20),'TEMPAT LAHIR'.ljust(10))
print('----------------------------------------------------------------------')

for i in mhs:
    data = i.split(':')
    nim = data[0]
    nama = data[1]
    TGL = data[2]
    tgl = TGL.split('-')
    TGLbaru = '{0}/{1}/{2}'.format(tgl[0],tgl[1],tgl[2])
    TempatLahir = data[3]

    print(nim.ljust(10),nama.ljust(20),TGLbaru.ljust(20),TempatLahir.ljust(10))
print('----------------------------------------------------------------------')
