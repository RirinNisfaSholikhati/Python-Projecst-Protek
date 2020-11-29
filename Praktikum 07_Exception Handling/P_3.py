#Praktikum3_P07_ExceptionHandling
file = open("E:/data1.txt", "r")
try:
    sum = 0
    for data in file:
        sum = sum + int(data)
    print(sum)
except ValueError:
    print('Input tidak valid')
