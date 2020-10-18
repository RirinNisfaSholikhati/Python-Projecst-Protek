jarak_AC = 795
Perliter = 12
kapasitas = 50

TotalBensin = jarak_AC/Perliter
minMengisi = TotalBensin/kapasitas
frekuensi = int(minMengisi)

print('Pak Budi harus mengisi bensin sebanyak : '+str(frekuensi) +'kali')
