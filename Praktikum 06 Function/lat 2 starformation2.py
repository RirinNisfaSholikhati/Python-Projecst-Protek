def starformation2(x):
    string = ""
    bar = x
    while bar >= 0:
        
        kol = bar

        while kol > 0:
            string = string + "*"
            kol = kol - 1

        string = string + "\n"
        bar = bar - 1
    print(string)
    
starformation2(4)
