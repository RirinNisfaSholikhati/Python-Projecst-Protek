kode_karyawan = int(input('Masukkan Kode Karyawan :'))
nama_karyawan = input('Masukkan Nama Karyawan:')
golongan = input('Masukkan Golongan:')

print('====================================')

print('STRUK RINCIAN GAJI KARYAWAN')

print('------------------------------------')

print('Nama Karyawan :' + nama_karyawan + '(Kode Karyawan:' + str (kode_karyawan) + ')')
print('Golongan      :' + golongan)

print('------------------------------------')

if (golongan == 'A'):
    GajiPokok = 10000000
    Potongan = 2.5
    JmlPotongan = 2.5 / 100 * 10000000
    GajiBersih = 10000000 - JmlPotongan
elif (golongan ==  'B'):
    GajiPokok = 8500000
    Potongan = 2.0
    JmlPotongan = 2.0/ 100 * 8500000
    GajiBersih = 8500000 - JmlPotongan
elif (golongan ==  'C'):
    GajiPokok = 7000000
    Potongan = 1.5
    JmlPotongan = 1.5/ 100 * 7000000
    GajiBersih = 7000000 - JmlPotongan
elif (golongan ==  'D'):
    GajiPokok = 5500000
    Potongan = 1.0
    JmlPotongan = 1.0/ 100 * 5500000
    GajiBersih = 5500000- JmlPotongan

print('GajiPokok: Rp' + str (GajiPokok))
print('Potongan(' + str (Potongan) + '%): Rp' + str(JmlPotongan))

print ('--------------------------------- -')
print('GajiBersih: Rp' + str (GajiBersih))
