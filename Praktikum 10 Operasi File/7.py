#P10_OperasiFile_7(MengembalikanTeksAsli)

huruf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
         'o','p','q','r','s','t','u','v','w','x','y','z']
n = int(input('Masukkan keyword n (dalam angka): '))


def SandiChipper(text,n):
  text = text.lower()
  hasil = ''
  for kar in text:
    if kar in huruf:
      index_old = huruf.index(kar)
      index_new = (index_old + n ) % 26
      kar_baru = huruf[index_new]
      hasil = hasil.upper() + kar_baru 
    else:
       hasil = hasil.upper() + ' ' 
  return hasil.upper()

file = input('Masukkan nama file hasil penyandian (file txt): ')
baca = open(file,'r')
teks = baca.readlines()
text=''.join(teks)

text_hasil = text
print('Hasil penyandian teks adalah :', text)

text_Asli = SandiChipper(text_hasil,-n)
print('Teks Asli :',text_Asli)

fileasli=open('fileOutput7.txt','w')
fileasli.write(str(text_Asli))
fileasli.close()                    
baca.close()
