pessoas = []
dados = []
maior = menor = 0

while True:
    dados.append(input("Digite o nome: "))
    dados.append(float(input("Digite o peso: ")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    resp = input("Deseja continuar [S/N]: ").upper()[0]
    if resp in "Nn":
        break

print(" " * 1)
print(f"Foram cadastradas {len(pessoas)} pessoas")
print(f"O maior peso foi de {maior}kg, as pessoas foram: ", end="")
for p in pessoas:
    if p[1] == maior:
        print(f"{p[0]}", end=" ")
print(f"\nO menor peso foi de {menor}kg, as pessoas foram: ",end="")
for p in pessoas:
    if p[1] == menor:
        print(f"{p[0]}",end=" ")
