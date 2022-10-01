from random import choice
print("Digite o nome dos 4 alunos!")
n1 = input()
n2 = input()
n3 = input()
n4 = input()
lista = [n1, n2, n3, n4]
print(f"O aluno sorteado foi o: {choice(lista)}")