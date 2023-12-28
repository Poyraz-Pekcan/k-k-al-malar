from itertools import permutations
import time

başla = time.time()

kelime1 = input("Birinci kelimeyi giriniz: ")
kelime2 = input("İkinci kelimeyi giriniz: ")
harfler = kelime1 + kelime2

txt = open(r"C:\Users\Poyraz\Downloads\TDK_Sözlük_Kelime_Listesi.txt", "r", encoding="UTF-8")
veri = txt.read()
sözlük = veri.split("\n")

#the part that actually makes it worse
for kelime in sözlük:
    if len(kelime) != len(harfler):
        sözlük.remove(kelime)

permütasyonlar = [''.join(p) for p in permutations(harfler)]

print("Arama başlıyor...")
for permütasyon in permütasyonlar:
    if permütasyon in sözlük:
        print(permütasyon)
print("Arama bitti!")

bitir = time.time()
print(f"Çalışma süresi {bitir - başla}s")