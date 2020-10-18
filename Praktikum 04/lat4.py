jamBerangkat = 6
istirahat = 0.75

jarak_AB = 125
kec_ab = 62
waktu_AB = 125/62

jarak_BC = 256
kec_bc = 70
waktu_BC = 256/70


durasiWaktu = waktu_AB + waktu_BC + istirahat
TotalWaktu = int(durasiWaktu)
jamSampai = jamBerangkat + TotalWaktu

print('Pak Amir sampai dikota C pada pukul : '+str(jamSampai)+'siang')
