from random import shuffle
lista = []
while len(lista) < 4:
    nome_aluno = input("Digite o nome de 4 alunos: ")
    lista += nome_aluno
shuffle(lista)
print(f"A ordem para a apresentação será:\n{lista}")

