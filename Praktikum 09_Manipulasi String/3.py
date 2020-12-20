#P09_ManipulasiString_3

def bintang(n):
    x = n - 3
    y = n - 4
    for i in range(x):
        print(('*'*(1+2*i)).center(1+2*x))
    for j in reversed(range(y)):
        print(('*'*(1+2*j)).center(1+2*x))
        
bintang(7)

