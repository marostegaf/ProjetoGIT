valores = [[], []]

for i in range(7):
    valor = int(input("Digite um valor: "))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()

print(" " * 1)
print(f"Os valores pares foram: {valores[0]}")
print(f"Os valores impares foram: {valores[1]}")
