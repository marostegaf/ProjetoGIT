from datetime import date
anoatual = date.today().year

pessoas = []
maior = []
menor = []

for i in range(1, 8):
    a = int(input(f"Digite o ano de nascimento da {i}º pessoa: "))
    pessoas.append(a)

for c in range(len(pessoas)):
    if anoatual - pessoas[c] >= 21:
        maior.append(pessoas[c])
    else:
        menor.append(pessoas[c])

print(f"{len(maior)} pessoa(s) já são de maior: {maior}")
print(f"{len(menor)} pessoa(s) ainda são de menor: {menor}")
