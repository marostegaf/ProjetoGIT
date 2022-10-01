import random
alunos = []
while len(alunos) < 4:
    nome_aluno = input("Nome do Aluno: ")
    alunos.append(nome_aluno)
print(f"O aluno sorteado foi: {random.choice(alunos)}")
