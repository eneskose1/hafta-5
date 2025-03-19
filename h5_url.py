def tarih_olustur(t1, t2):
    tarih1 = t1.split('.')
    tarih2 = t2.split('.')
    yıl1 = int(tarih1[-1])
    yıl2 = int(tarih2[-1])
    ay1 = int(tarih1[-2])
    ay2 = int(tarih2[-2])
    gun1 = int(tarih1[-3])
    gun2 = int(tarih2[-3])
    yıl1 = "{:04d}".format(yıl1)
    yıl2 = "{:04d}".format(yıl2)
    ay1 = "{:02d}".format(ay1)
    ay2 = "{:02d}".format(ay2)
    gun1 = "{:02d}".format(gun1)
    gun2 = "{:02d}".format(gun2)
    return yıl1, yıl2, ay1, ay2, gun1, gun2
t1 = input("Birinci yılı giriniz : (GG.AA.YYYY) ")
t2 = input("İkinci yılı giriniz : (GG.AA.YYYY) ")
yıl1, yıl2, ay1, ay2, gun1, gun2 = tarih_olustur(t1, t2)
print('Girdiğiniz Yıllar :', t1, t2)
kategory = ['finans', 'spor', 'siyaset']
habersiteleri = ['akşam', 'sabah','Takvim']
for m in habersiteleri:
    gazete = 'www.{}.com'.format(m)
    for k in kategory:
        for i in range(int(yıl1), int(yıl2) + 1):
            for j in range(1,12,1):
                for gun in range(1,30,1):
                    print('{}/{}/{}/{}/{}'.format(gazete, k, str(i).zfill(4), str(j).zfill(2), str(gun).zfill(2)))
# The second definition of tarih_olustur was indented incorrectly, causing the error.
# It has been moved to the outer scope, aligning with other function definitions.
def tarih_olustur(t1, t2):
    tarih1 = t1.split('.')
    tarih2 = t2.split('.')
    yıl1 = int(tarih1[-1])
    yıl2 = int(tarih2[-1])
    ay1 = int(tarih1[-2])
    ay2 = int(tarih2[-2])
    gun1 = int(tarih1[-3])
    gun2 = int(tarih2[-3])
    yıl1 = "{:04d}".format(yıl1)
    yıl2 = "{:04d}".format(yıl2)
    ay1 = "{:02d}".format(ay1)
    ay2 = "{:02d}".format(ay2)
    gun1 = "{:02d}".format(gun1)
    gun2 = "{:02d}".format(gun2)
    return yıl1, yıl2, ay1, ay2, gun1, gun2

def url_olustur(habersiteleri, kategoriler, yıl1, yıl2):
    for m in habersiteleri:
        gazete = 'www.{}.com'.format(m)
        for k in kategoriler:
            for i in range(int(yıl1), int(yıl2) + 1):
                for j in range(1, 13):
                    for gun in range(1, 30):
                        print('{}/{}/{}/{}/{}'.format(gazete, k, str(i).zfill(4), str(j).zfill(2), str(gun).zfill(2)))

t1 = input("Birinci yılı giriniz : (GG.AA.YYYY) ")
t2 = input("İkinci yılı giriniz : (GG.AA.YYYY) ")
yıl1, yıl2, ay1, ay2, gun1, gun2 = tarih_olustur(t1, t2)
print('Girdiğiniz Yıllar :', t1, t2)

kategoriler = ['finans', 'spor', 'siyaset']
habersiteleri = ['haberturk', 'hurriyet','sabah']

url_olustur(habersiteleri, kategoriler, yıl1, yıl2)
