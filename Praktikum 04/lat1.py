#variable assignment
jamMulai = 6
menitMulai = 00

jamSelesai = 23
menitSelesai = 50

#perhitungan
jamSewa = jamSelesai - jamMulai
menitSewa = menitSelesai - menitMulai

durasiSewa = jamSewa + menitSewa / 60

totalSewa = int(durasiSewa)

#tarif sewa untuk 12 jam pertama 200000
totalTarif = 200000 + (10000*(totalSewa -12))

print('Tarif yang dibayarkan untuk sewa mobil adalah : ' + str(totalTarif))
