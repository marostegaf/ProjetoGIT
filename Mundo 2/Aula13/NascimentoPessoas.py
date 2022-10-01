from datetime import date
anoatual = date.today().year
anos = []
maior = []
dez = anoatual - 18
for i in range(2):
    a = int(input("Digite o ano de nascimento de 7 pessoas: "))
    anos.append(a)

for i in range(7):
    if anos[i] <= 2004:
        maior.append(anos[a])
print("Os maiores de idade são: {maior}")
