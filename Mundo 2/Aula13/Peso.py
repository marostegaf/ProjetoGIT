pessoas = []


for i in range(1, 6):
    p = float(input(f"Digite o peso da {i}ª pessoa: "))
    pessoas.append(p)

maior = pessoas[0]
menor = pessoas[0]

for c in range(5):
    if pessoas[c] < menor:
        menor = pessoas[c]
    else:
        maior = pessoas[c]

print(f"Pessoa com maior peso: \033[32m{maior:.2f}\033[mkg")
print(f"Pessoa com menor peso: \033[32m{menor:.2f}\033[mkg")
