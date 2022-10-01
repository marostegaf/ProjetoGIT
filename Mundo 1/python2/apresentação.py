from random import shuffle
print("Digite o nome dos alunos: ")
a = str(input())
b = str(input())
c = str(input())
d = str(input())
lista = [a, b, c, d]
shuffle(lista)
print(f"A apresentação vai ser na seguinte ordem:\n{lista}")