#P10_OperasiFile_6(SandiChipper)

abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
         'o','p','q','r','s','t','u','v','w','x','y','z']
n = int(input('Masukkan keyword n (dalam angka): '))


def SandiChipper(text,n):
  text = text.lower()
  hasil = ''
  for kar in text:
    if kar in abjad:
      index_awal = abjad.index(kar)
      index_baru = (index_awal + n ) % 26
      kar_baru = abjad[index_baru]
      hasil = hasil.upper() + kar_baru 
    else:
       hasil = hasil.upper() + ' ' 
  return hasil.upper()

file = input('Masukkan nama file yang ingin disandikan (file txt): ')
baca = open(file,'r')
teks = baca.readlines()
text=''.join(teks)

text_hasil = SandiChipper(text,n)
print('Hasil penyandian teks adalah :', text_hasil)

filesandi=open('fileOutput6.txt','w')
filesandi.write(str(text_hasil))
filesandi.close()                    
baca.close()
