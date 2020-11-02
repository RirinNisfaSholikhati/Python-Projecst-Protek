def jumlah(*myData):
    sum = 0
    for data in myData:
        sum += data
    print('Jumlah totalnya:',sum)
    return  
   


def rerata(*myData):
    sum = 0
    i = 0
    for data in myData:
        sum += data
        i += 1
    
    rata2 = sum/i       
    print('Rata ratanya: ',rata2)
    return myData



def NilaiMax(*myData):
    terbesar = 0
    for nilai in myData:
        if  nilai > terbesar:
            terbesar = nilai        
    print('Nilai Terbesar: ',terbesar)
    return terbesar
    

def NilaiMin(*myData):
    terkecil = 99
    for nilai in myData:
        if  nilai < terkecil:
            terkecil = nilai        
    print('Nilai Terkecil: ',terkecil)
    return terkecil
