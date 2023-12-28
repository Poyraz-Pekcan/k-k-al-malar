ss = 0
bos = 0
yanlis = 0
net = 0
dogru = 0
ders = ""

while 1 == 1:
  ss = 0
  bos = 0
  yanlis = 0
  net = 0
  dogru = 0
  ders = ""

  ders = input("Dersi girin: ")
  if ders == "çıkış":
    exit()
  ss = input("Soru sayısını girin: ")
  while True:
    try:
      int(ss)
    except:
      pass
    else:
      ss = int(ss)
      break
    ss = input("lütfen sayı girin: ")
    
  print("Boş girmek için \"b\", yanlış girmek için \"y\", sonucu görmek için \"yazdır\" yazın.")
  while True:
    girdi = input()
    if girdi == "b":
      bos += 1
    elif girdi == "y":
      yanlis += 1
    elif girdi == "yazdır":
      break
    elif girdi == "çıkış":
      exit()
    else:
      print("geçersiz")
  dogru = ss - bos - yanlis
  net = ss - bos - yanlis * 1.25
  print()
  print(ders)
  print("Doğru: " + str(dogru))
  print("Yanlış: " + str(yanlis))
  print("Boş: " + str(bos))
  print("Net: " + str(net))
  print()
