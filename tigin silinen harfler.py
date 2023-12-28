from itertools import permutations

txt = open(r"C:\Users\Poyraz\Downloads\TDK_Sözlük_Kelime_Listesi.txt", "r", encoding="UTF-8")
veri = txt.read()
sözlük = veri.split("\n")

alfabe = "abcçdefghıijklmnoçprsştuüvyz"

girdi1 = input("Birinci harf dizisini giriniz: ")
girdi2 = input("İkinci harf dizisini giriniz: ")

for i in alfabe:
    for j in alfabe:
        g1, g2 = girdi1 + i + j, girdi2 + i + j
        g1perm = list(set([''.join(p) for p in permutations(g1)]))
        g2perm = list(set([''.join(p) for p in permutations(g2)]))

        for p1, p2 in zip(g1perm, g2perm):
            if p1 in sözlük and p2 in sözlük:
                print(f"Birinci kelime {p1}")
                print(f"İkinci kelime {p2}")
                print(f"İkisinden de silinen harfler {i} ve {j}")