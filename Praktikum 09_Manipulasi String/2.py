#P09_ManipulasiString_2

def bintang(n):
    x = n
    for i in range(x):
        print(('*'*(1+2*i)).center(1+2*x))

bintang(4)
