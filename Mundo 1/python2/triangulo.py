'''
op = float(input("Digite o comprimento do cateto OP: "))
adj = float(input("Digite o comprimento do cateto ADJ: "))
hip = (op ** 2 + adj ** 2) ** (0.5)
print(f"Cateto Oposto: {op}\nCateto Adjacente: {adj}\nHipotenusa: {hip}")
'''
#ou

from math import hypot
op = float(input("Digite o comprimento do cateto OP: "))
adj = float(input("Digite o comprimento do cateto ADJ: "))
hip = math.hypot(op, adj)
print(f"Cateto Oposto: {op}\nCateto Adjacente: {adj}\nHipotenusa: {hip:2.f}")

