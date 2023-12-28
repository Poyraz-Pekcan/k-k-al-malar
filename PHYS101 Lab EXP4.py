#sabitler
timeError = 0.05
dm, dh0, dh1, dh2max = 0.001, 0.001, 0.001, 0.001
dx, dL = 0.002, 0.002
centi = 0.01
kilo = 0.001
g = 9.8

#hata payı hesaplama fonksiyonu
def hpçarpma(da, a, db, b):
    return da / a + db / b

#girdiler
k = float(input("k: "))
dk = float(input("dk: "))
x = float(input("x: ")) * centi
t = float(input("t: "))
dt = t * timeError
h2max = float(input("h2max: ")) * centi
m = float(input("m: ")) * kilo
L = float(input("L: ")) * centi
h0 = float(input("h0: ")) * centi
h1 = float(input("h1: ")) * centi

#işlemler
#1
v = L/t
dv = v * hpçarpma(dL, L, dt, t)


#2
Us = 0.5 * k * x**2
dUs = Us * hpçarpma(dk, k, 2 * dx, x)

Ug0 = m * g * h0
dUg0 = Ug0 * hpçarpma(dm, m, dh0, h0)

E0 = Us + Ug0
dE0 = dUs + dUg0

#3
K = 0.5 * m * v**2
dK = K * hpçarpma(dm, m, 2 * dv, v)

Ug1 = m * g * h1
dUg1 = Ug1 * hpçarpma(dm, m, dh1, h1)

E1 = K + Ug1
dE1 = dK + dUg1

#4
Ug2 = m * g * h2max
dUg2 = Ug2 * hpçarpma(dm, m, dh2max, h2max)

E2 = Ug2
dE2 = dUg2

#5
Elost = abs(E0 - E2) / E0 * 100

#çıktılar
print()
print(f"v: {v:e}m/s ± Δ{dv:e}m/s")
print()
print(f"Us: {Us:e}J ± Δ{dUs:e}J")
print(f"Ug,0: {Ug0:e}J ± Δ{dUg0:e}J")
print(f"E0: {E0:e}J ± Δ{dE0:e}J")
print()
print(f"K: {K:e}J ± Δ{dK:e}J")
print(f"Ug,1: {Ug1:e}J ± Δ{dUg1:e}J")
print(f"E1: {E1:e}J ± Δ{dE1:e}J")
print()
print(f"E2 = Ug2: {E2:e}J ± Δ{dE2:e}J")
print()
print(f"Energy loss is {Elost:e}%")
