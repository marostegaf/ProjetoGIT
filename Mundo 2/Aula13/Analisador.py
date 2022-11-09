somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0

for p in range(1, 5):
    print(f"{p}ª Pessoa")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1

médiaidade = somaidade / 4
print("\033[35m=\033[m" * 48)
print(f"A média de idade do grupo é: {médiaidade:.0f}")
print(f"O homem mais velho se chama {nomevelho} e tem {maioridadehomem} anos")
print(f"Ao todo são {totmulher20} mulheres com menos de 20 anos!")
print("\033[35m=\033[m" * 48)
