#P10_OperasiFile_3

file = open("dataOutput2.txt","r")
myfile = file.readlines()

data = {}
dataMhs = []

for a in range(len(myfile)):
    b = myfile[a].split('|')
    b[2] = b[2].replace('\n','')

    data = {'nim' : b[0], 'nama' : b[1], 'alamat' : b[2]}
    dataMhs.append(data)

  
print(dataMhs)
