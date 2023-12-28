import math
#Sırası değişmeden farklı işlemler kullanılarak 100 elde edilecek sayı
SAYI = "29102023"
OlsıAyrıştırmalar = []

#İşimize yarayacak fonksiyonlar
#Bir listedeki tüm strleri inte çeviren bir fonksiyon
def Lint(liste):
    çıktı = []
    for i in liste:
        çıktı.append(int(i))
    return çıktı

#Bir listedeki elemanları birer birer başka bir listeye ekleyen bir fonksiyon
def ekle(eklenilen, eklenen):
    for i in eklenen:
        eklenilen.append(i)

#Soru için gerekli işlemleri fonksiyon olarak tanımlyoruz
def toplama(a, b):
    return a + b

def çıkarma(a, b):
    return a - b

def çarpma(a, b):
    return a * b

def bölme(a, b):
    return a / b 

def faktöriyel(a):
    return math.factorial(a)

#Bir listeye
def işle(liste, fonksiyon):
    return fonksiyon(liste[0], liste[2])

işlemler = [toplama, çıkarma, çarpma, bölme, faktöriyel]

#İşlemler yapılmadan önce sayıları her türlü ayırıyoruz
#Hepsi ayrı
OlsıAyrıştırmalar.append(Lint(list(SAYI)))

#Bir sayı iki basamaklı, kalanı tek basamaklı
for i in range(0,len(SAYI)-1):
    if len(str(int(SAYI[i: i+2]))) == 1:
        continue
    OlsıAyrıştırmalar.append(Lint(list(SAYI[:i]) + [SAYI[i: i + 2]] + list(SAYI[i+2:])))


#İki sayı iki basamaklı, kalanı tek basamaklı
for i in range(0,len(SAYI)-3):
    geçiciliste1 = []
    if len(str(int(SAYI[i: i+2]))) == 1:
        continue
    ekle(geçiciliste1, Lint(list(SAYI[:i]) + [SAYI[i: i+2]]))
    for j in range(i+2, len(SAYI)):
        geçiciliste2 = []
        if len(str(int(SAYI[j: j + 2]))) == 1:
            continue
        ekle(geçiciliste2, Lint(list(SAYI[i + 2: j]) + [SAYI[j: j + 2]] + list(SAYI[j + 2:])))
        OlsıAyrıştırmalar.append(geçiciliste1 + geçiciliste2)

#Bir sayı üç basamaklı, kalanı tek basamaklı
for i in range(0,len(SAYI)-2):
    if len(str(int(SAYI[i: i+3]))) == 2:
        continue
    OlsıAyrıştırmalar.append(Lint(list(SAYI[:i]) + [SAYI[i: i+3]] + list(SAYI[i+3:])))

for ayrıştırma in OlsıAyrıştırmalar:
    pass



