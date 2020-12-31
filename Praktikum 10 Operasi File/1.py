#P10_OperasiFile_1

myfile = open ('angka.txt','r')    
angka = myfile.readlines()
genap = []
ganjil = []

for i in range(len(angka)):
    if ('\n' in angka[i] == True):
        angka[i].remove('\n')  
        if (int(angka[i]) % 2 == 0):
            genap.append(angka[i])
        else:
            ganjil.append(angka[i])
    else:
        if (int(angka[i]) % 2 == 1):
            ganjil.append(angka[i])
        else:
            genap.append(angka[i])     
            
print('Banyak bilangan genap:',len(genap))        
print('Banyak bilangan ganjil:',len(ganjil))
