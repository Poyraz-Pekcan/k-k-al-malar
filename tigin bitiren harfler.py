txt = open(r"C:\Users\Poyraz\Downloads\TDK_Sözlük_Kelime_Listesi.txt", "r", encoding="UTF-8")
veri = txt.read()
sözlük = veri.split("\n")

alfabe = "abcçdefghıijklmnoçprsştuüvyz"

harf1 = input("Birinci harfleri giriniz: ")
harf2 = input("İkinci harfleri giriniz: ")
harf3 = input("Üçüncü harfleri giriniz: ")

for i in alfabe:
    for j in alfabe:
        for k in alfabe:
            cevap = i + j + k
            if harf1 + cevap in sözlük and harf2 + cevap in sözlük and harf3 + cevap in sözlük:
                print(harf1 + cevap)
                print(harf2 + cevap)
                print(harf3 + cevap)
                print("Hepsini bitiren üç harf:", cevap)
            