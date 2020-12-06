#P08_PythonProject_3

data=[]
i = 1

for i in range(4):
    nama = str(input('Masukkan Nama Mahasiswa:'))
    data.append(nama)
    i+=1
    data.sort()
print('--------------------------')
jmlh = len(data[0]) 
print(data[0],'(',jmlh,'karakter)')
jmlh = len(data[1]) 
print(data[1],'(',jmlh,'karakter)')
jmlh = len(data[2]) 
print(data[2],'(',jmlh,'karakter)')
jmlh = len(data[3]) 
print(data[3],'(',jmlh,'karakter)')
