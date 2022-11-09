n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
med = (n1+n2)/2
if med < 5:
    print(f"Aluno com média de {med}: \033[31mREPROVADO\033[m")
elif med >= 5 and med <= 6.9:
    print(f"Aluno com média de {med}: \033[36mRecuperação\033[m")
else:
    print(f"Aluno com média de {med}: \033[32mAprovado\033[m")
