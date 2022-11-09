pt = int(input("Digite o primeiro termo de uma progressão aritmética: "))
r = int(input("Digite a razão dessa progressão aritmética: "))
#t = int(input("Quantos termos você deseja visualizar: "))
pa = []
for i in range(10):
    pa.append(pt)
    pt += r
print(f"PA: {pa}")
