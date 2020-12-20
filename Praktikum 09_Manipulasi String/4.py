#P09_ManipulasiString_4

def shuffleString(x,n):
    daftar = []
    i = 0
    while (i < n) :
        import random
        a = list(x)
        y = ''.join(random.sample(a,len(a)))
        if( y not in daftar):
            daftar += [y]
            i += 1
    print(daftar)

shuffleString("aku",3)    
shuffleString("aku",4)
shuffleString("aku",5)
