#P08_PythonProject_7

buah = {'apel' : 5000,
        'jeruk' : 8500,
        'mangga' : 7800,
        'duku' : 6500}

def palingMahal(dictionary):
    nama = list(dictionary.keys())
    harga = tuple(dictionary.values())

    hargaMahal = max(harga)
    indexHargaTermahal = harga.index(hargaMahal)
    print(nama[indexHargaTermahal])

palingMahal(buah)
    
