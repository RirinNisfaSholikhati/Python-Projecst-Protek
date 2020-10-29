kode_karyawan = int(input('Masukkan Kode Karyawan :'))
nama_karyawan = input('Masukkan Nama Karyawan:')
golongan = input('Masukkan Golongan:')
status = input('Masukkan status(1:menikah, 2: belum):')
if(status == '1'):
    Jml_Anak = int(input('Masukkan jumlah anak :'))
    TunjanganSuamiIstri = 10/100
    TunjanganAnak = 5 / 100 * Jml_Anak
    Status_Menikah = 'Sudah Menikah'
else:
    Jml_Anak = 0
    TunjanganSuamiIstri = 0
    TunjanganAnak = 0
    Status_Menikah = 'Belum Menikah'


print('====================================')

print('STRUK RINCIAN GAJI KARYAWAN')

print('------------------------------------')

print('Nama Karyawan:' + nama_karyawan + '(Kode Karyawan:' + str (kode_karyawan)+')')
print('Golongan:' + golongan)
print('Status Menikah:'+ Status_Menikah)
print('Jumlah Anak:'+ str(Jml_Anak))
    
print('------------------------------------')

if (golongan == 'A'):
    GajiPokok = 10000000
    Potongan = 2.5
    JmlPotongan = 2.5 / 100 * 10000000
    JmlTunjanganSuamiIstri = 10000000 * TunjanganSuamiIstri
    JmlTunjanganAnak = 10000000 * Jml_Anak
    GajiKotor = GajiPokok + JmlTunjanganSuamiIstri + JmlTunjanganAnak
    GajiBersih = GajiKotor - JmlPotongan
    
elif (golongan ==  'B'):
    GajiPokok = 8500000
    Potongan = 2.0
    JmlPotongan = 2.0/ 100 * 8500000
    JmlTunjanganSuamiIstri = 8500000 * TunjanganSuamiIstri
    JmlTunjanganAnak = 8500000 * Jml_Anak
    GajiKotor = GajiPokok + JmlTunjanganSuamiIstri + JmlTunjanganAnak
    GajiBersih = GajiKotor - JmlPotongan
    
elif (golongan ==  'C'):
    GajiPokok = 7000000
    Potongan = 1.5
    JmlPotongan = 1.5/ 100 * 7000000
    JmlTunjanganSuamiIstri = 7000000 * TunjanganSuamiIstri
    JmlTunjanganAnak = 7000000 * Jml_Anak
    GajiKotor = GajiPokok + JmlTunjanganSuamiIstri + JmlTunjanganAnak
    GajiBersih = GajiKotor - JmlPotongan
    
elif (golongan ==  'D'):
    GajiPokok = 5500000
    Potongan = 1.0
    JmlPotongan = 1.0/ 100 * 5500000
    JmlTunjanganSuamiIstri = 5500000 * TunjanganSuamiIstri
    JmlTunjanganAnak = 5500000 * Jml_Anak
    GajiKotor = GajiPokok + JmlTunjanganSuamiIstri + JmlTunjanganAnak
    GajiBersih = GajiKotor - JmlPotongan
   
print('GajiPokok: Rp' + str (GajiPokok))
print('Tunjangan Istri/Suami: Rp' + str(JmlTunjanganSuamiIstri))
print('Tunjangan Anak: Rp' + str(JmlTunjanganAnak))

print('------------------------------------ +')

print('Gaji Kotor: Rp' + str(GajiKotor))
print('Potongan(' + str (Potongan) + '%): Rp' + str(JmlPotongan))

print ('----------------------------------- -')
print('GajiBersih: Rp' + str (GajiBersih))
