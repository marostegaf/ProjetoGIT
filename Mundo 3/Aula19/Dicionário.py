aluno = {}

aluno["Nome"] = input("Nome: ")
aluno["Média"] = float(input("Média: "))

if aluno["Média"] >= 7:
    aluno["Situação"] = "Aprovado"
elif 5 <= aluno["Média"] < 7:
    aluno["Situação"] = "Recuperação"
else:
    aluno["Situação"] = "Reprovado"

print("=" * 45)
for i, j in aluno.items():
    print(f" - {i} é igual a {j}") 
