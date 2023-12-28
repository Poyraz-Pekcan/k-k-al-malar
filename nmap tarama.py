import os

print("NMAP PORT TARAMA")

ip = input("Port taraması yapmak istediğiniz ip adresini giriniz: ")
başlangıç_port = int(input("Kaçıncı porttan aramaya başlasın? "))
bitiş_port = int(input("Kaçıncı portta aramayı bitirsin? "))
sV = input("Versiyon taraması olsun mu? (evet) ")

if sV == "evet":
    print(os.system(f"nmap {ip} -sV -p {başlangıç_port}-{bitiş_port}"))
else:
    print(os.system(f"nmap {ip} -p {başlangıç_port}-{bitiş_port}"))