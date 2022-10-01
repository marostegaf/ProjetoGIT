pessoa = []
cadastro = {}
med = 0
mulheres = []

while True:
    cadastro.clear
    cadastro["Nome"] = input("Nome: ")
    while True:
        cadastro["Sexo"] = input("Sexo: ").upper()[0]
        if cadastro["Sexo"] not in "MmFf":
            print("Digite novamente... ", end="")
        else:
            if cadastro["Sexo"] in "Ff":
                mulheres.append(cadastro["Nome"])
            break
    cadastro["Idade"] = int(input("Idade: "))
    med += cadastro["Idade"]
    pessoa.append(cadastro.copy())

    while True:
        resp = input("Deseja continuar [S/N]: ")
        if resp in "NnSs":
            break
    if resp in "Nn":
        break

print("=" * 45)
print(f"Foram cadastradas: {len(pessoa)} pessoas")
print("=" * 45)
print(f"A média de idade foi de: {med/len(pessoa):.0f}")
print("=" * 45)
print("Mulheres cadastradas: ", end="")

for i in range(len(mulheres)):
    print(f"{mulheres[i]}", end=" ")
print()
print("=" * 45)
print("Pessoas acima da média: ")
for p in pessoa:
    if p["Idade"] >= (med/len(pessoa)):
        for k, v in p.items():
            print(f"{k} = {v}; ", end="")
        print()
