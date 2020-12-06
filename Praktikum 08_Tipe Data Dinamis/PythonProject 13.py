#P08_PythonProject_13

nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	      {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

def NilaiAkhir(nilaiMhs):
    global Nilaix
    Nilaix = 0

    for r in nilaiMhs:
        nilaiMid = r.get('mid')
        nilaiAkhir = r.get('uas')
        nilaiTotal = (nilaiMid + 2*nilaiAkhir)/3

        if(nilaiTotal > Nilaix):
            Nilaix = nilaiTotal
            data = {}
            data['nim'] = r.get('nim')
            data['nama'] = r.get('nama')
    return data

nilaiTertinggi = NilaiAkhir(nilaiMhs)
print('Mahasiswa yang bernama {0} dengan NIM {1} mendapat nilai akhir tertinggi'.format(nilaiTertinggi['nama'], nilaiTertinggi['nim']))
