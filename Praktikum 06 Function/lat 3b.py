n = 10
r = 7
def faktorial(x):
    if x == 1:
        return 1
    elif x == 0:
        return 1
    else:
        return(x*faktorial(x-1))
hasil = (faktorial(n)/(faktorial(r)*faktorial(n-r)))
print('Hasil Permutasi adalah:',hasil)
