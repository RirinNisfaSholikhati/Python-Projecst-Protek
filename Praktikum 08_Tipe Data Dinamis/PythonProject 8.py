#P08_PythonProject_8

buah = {'apel' : 5000,
        'jeruk' : 8500,
        'mangga' : 7800,
        'duku' : 6500}

def HargaRerataBuah(buah):
    harga = list(buah.values())
    Rerata = sum(harga) / len(harga)
    return Rerata

x = HargaRerataBuah(buah)
print('Rerata harga buah per/ satuan adalah:',x)
