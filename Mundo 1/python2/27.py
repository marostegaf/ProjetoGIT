from random import choice, shuffle
lista = []
while len(lista) < 4:
    nome_aluno = input("Digite o nome de 4 alunos: ")
    lista.append(nome_aluno)
print(f"O aluno sorteado: {choice(lista)}")

