IDN = int(input("Masukkan nilai Bhs Indonesia : "))
IPA = int(input("Masukkan nilai IPA : "))
MTK = int(input("Masukkan nilai Matematika : "))
        
if (IDN > 100 or IDN < 0):
    print ('Maaf input yang ada tidak valid')
elif (IPA > 100 or IPA < 0):
    print ('Maaf input yang ada tidak valid')
elif (MTK > 100 or MTK < 0):
    print ('Maaf input yang ada tidak valid')

elif (IDN > 60 and IPA > 60 and MTK > 70):
    print("Status Kelulusan : LULUS")
else:
    print("Status Kelulusan : Tidak LULUS")
    
