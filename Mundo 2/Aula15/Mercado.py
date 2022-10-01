tot = totmil = menor = cont = 0
barato = " "

while True:
    prod = input("Nome do produto: ")
    preço = float(input("Preço do produto: R$"))
    cont += 1
    tot += preço
    if preço >= 1000:
        totmil += 1

    if cont == 1 or preço < menor:
        menor = preço
        barato = prod
    else:
        if preço < menor:
            menor = preço
            barato = prod

    resp = " "
    while resp not in "SsNn":
        resp = input("Quer continuar [S/N]: ").strip().upper()[0]

    if resp in "Nn":
        break

print("="*50)
print("           Fim do programa")
print(f"Total da compra: R$\033[32m{tot:.2f}\033[m")
print(f"\033[32m{totmil}\033[m produtos custando mais de R$1000 reais")
print(f"Produto mais barato: [\033[32m{barato}\033[m] e custa: R$\033[32m{menor:.2f}\033[m")
print("="*50)
