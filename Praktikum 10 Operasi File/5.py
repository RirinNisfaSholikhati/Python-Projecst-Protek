#P10_OperasiFile_5

file = open('Text5.txt','r')
data = []

for x in file.readlines():
    if('\n' in x):
        hapus = x.replace('\n','')
        angka = hapus.split('|')
        nilai = int(angka[0]) + int(angka[1])
        data.append(nilai)

    else:
        angka = x.split('|')
        nilai = int(angka[0]) + int(angka[1])
        data.append(nilai)
file.close()

hasil = open('HasilText5.txt','w')
for x in range(len(data)):
    hasil.write(str(data[x]) + '\n')
hasil.close()
