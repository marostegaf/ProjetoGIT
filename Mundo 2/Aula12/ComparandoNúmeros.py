n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 == n2:
    print(f"Os valores \033[36m{n1}\033[m e \033[36m{n2}\033[m são iguais!")
else:
    if n1 > n2:
        print(f"O primeiro valor \033[32m({n1})\033[m é maior que o segundo \033[31m({n2})!\033[m")
    else:
        print(f"O segundo valor \033[32m({n2})\033[m é maior que o primeiro valor \033[31m({n1})\033[m")
