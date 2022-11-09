emp = float(input("Qual o valor do empréstimo: "))
sal = float(input("Qual o seu salário: "))
anos = float(input("Em quantos anos você deseja quitar esse empréstimo: "))
parcela = emp/(anos*12)
if parcela > (0.30)*sal:
    print(f"Empréstimo negado, o valor excedeu o seu salário de: \033[31m{sal}\033[m e o seu empréstimo seria de: \033[31m{parcela:.2f}\033[m] ")
else:
    print(f"Empréstimo permitido, com parcelas de: \033[32m{parcela:.2f}\033[m")
