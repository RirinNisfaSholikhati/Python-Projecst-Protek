#P11_Datetime_01

from datetime import date

def diffDate(x):
    y = x.split('/')
    tgl1 = date(year = int(y[0]), month = int(y[1]), day = int(y[2]))
    tgl2 = date.today()
    selisih = tgl1 - tgl2
    print('Selisih Tanggal adalah ', selisih.days, ' hari')
    return

diffDate('2021/1/4')

