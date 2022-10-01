from random import randint
a = [0]*20

for i in range(20):
    a[i] = randint(0, 9)
print(a)
num = int(input("digite um número de dois digitos:"))
numdezena = num // 10
numuni = num % 10
ordem = [numdezena, numuni]
resp = []

for i in range(19, 0, -1):
    if ordem[0] == a[i]:
        ordem[0] = ordem[1]
        resp.append(i)
        if len(resp) == 2:
            break

if len(resp) == 2:
    print(resp)
else:
    print("não existe")