n1 = int(input("Digite a primeira nota do aluno: "))
n2 = int(input("Digite a segunda nota do aluno: "))
med = (n1 + n2)/2
if med >= 5:
    print(f"Parabéns, você passou de ano com a média de \033[32m{med}")
else:
    print(f"Você foi reprovado com a média de \033[31m{med}")
