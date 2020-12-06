#P08_PythonProject_1

data = []
i = 1
n = int(input('Masukkan banyak n:'))
for i in range(n):
    angka = int(input('Masukkan angka:'))
    data.append(angka)
    i+=1
data.sort(reverse=True)
print(data)
    
