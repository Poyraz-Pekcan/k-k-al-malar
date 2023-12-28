#even fibonacci numbers
fib = [1,1]
i = 2

while fib[-1] < 4000000:
    fib.append(fib[-1] + fib[-2])
    i += 1

çiftToplam = 0
for i in fib:
    if i % 2 == 0:
        çiftToplam += i

print(çiftToplam)
    