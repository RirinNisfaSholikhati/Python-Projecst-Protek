#P09_ManipulasiString_5


nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('===========================================================')
print('NIM'.ljust(10),'NAMA'.ljust(10),'N.MID'.rjust(10),'N.UAS'.rjust(10))
print('-----------------------------------------------------------')

for x in nilai:
    print(x['nim'].ljust(10),x['nama'].ljust(10),str(x['mid']).rjust(10),str(x['uas']).rjust(10))

print('-----------------------------------------------------------')
