#P08_PythonProject_2

def dataStat(x):
    a = sum(x)/len(x)
    b = max(x)
    c = min(x)  
    dataABC = [a,b,c]
    return dataABC

while True:
    n = int(input('Masukkan banyak angka:'))
    break

Nilai = []
i = 0

while(i < n):
    angka = int(input('Masukkan angka yang diinginkan:'))
    Nilai.append(angka)
    i += 1

printNilai = dataStat(Nilai)
print(printNilai)
    
    
