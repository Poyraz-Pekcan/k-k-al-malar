def num(number):
    if "." in number:
        return float(number)
    else:
        return int(number)
#q1
print("Multiply your inputs by 10 then add them together until their sum reaches 100")
product = 0

while product < 100:
    product += int(input()) * 10

print()

#q2
KeepGoing = True
while KeepGoing:
    print("Their sum is:", int(input("Enter first number: ")) + int(input("Enter second number: ")))
    if input("Do you want to do this again? [Yes/No] ") == "Yes":
        pass
    else:
        KeepGoing = False

print()

#q3
for i in range(1,101):
    if i % 2 != 0:
        print(i, end=", ")
print()

print()

#q4
def validInput4(str):
    while True:
        inp = input(str)
        try:
            num(inp)
        except:
            pass
        else:
            inp = num(inp)
            if inp > 0:
                return inp
print(f"Your input is {validInput4('Please enter a positive number: ')}")
print()

#q5
while True:
    inp = input("Please enter a number 1 through 100: ")
    try:
        num(inp)
    except:
        pass
    else:
        inp = num(inp)
        if 1 <= inp <= 100:
            break
print(f"Your input is {inp}")
print()

#q6
tuition = 8000
ZAM = 1.03
total = 8000
for i in range(1,10):
    tuition *= ZAM
    total += tuition
print(f"5 year tuition amount is {total:.2f}$")
print()

#q7
sum = 0
while True:
    number = num(input("Enter a positive to add to the sum (input a negative number to finish this task): "))
    if not number > 0:
        break
    sum += number
print(sum)
print()

#q8
def faktöriyel(n):
    if n == 0:
        return 1
    elif type(n) != int:
        return "Hata: Girdi 'int' değil"
    elif n < 0:
        return "Hata: Girdi 0'dan küçük"
    else:
        return n * faktöriyel(n - 1)

print(faktöriyel(num(input("Faktöriyelini görmek istediğiiz sayıyı giriniz: "))))
print()

#q9
length = 0
counter = 0

while True:
    inp = input("Enter a word: ")
    if inp == "":
        break
    length += len(inp)
    counter += 1

print(f"{length/counter:.0f}")
