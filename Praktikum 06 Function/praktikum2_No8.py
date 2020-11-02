def luasSegitiga2(a,t):
    global luas
    luas = a * t / 2
    print('luas segitiga',luas)
    return
luasSegitiga2(10,20)
luas1=luas
luasSegitiga2(15,45)
luas2= luas
total = luas1+luas2
print('Luas total kedua segitiga adalah ',total)
      

