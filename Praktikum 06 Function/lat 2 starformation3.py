def starformation3(x):
    string = ""
    bar1 = 1
    bar = x
    while bar1 < x:
        kol = bar1
        while kol > 0:
            string = string+ "*"
            kol = kol - 1
        string = string + "\n"
        bar1 = bar1 + 1
    
    while bar >= 0:
        kol = bar

        while kol > 0:
            string = string + "*"
            kol = kol - 1

        string = string + "\n"
        bar = bar - 1
    print(string)

starformation3(4)
