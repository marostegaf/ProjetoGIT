matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = terceira_coluna = segunda_linha = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]

for i in range(3):
    terceira_coluna += matriz[i][2]

# PEGAR O MENOR
for i in range(3):
    if matriz[1][i] > segunda_linha:
        segunda_linha = matriz[1][i]
    
print()
for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]:^5}]",end="")
    print()
print()

print(f"A soma dos valores pares foi de: {par}")
print(f"A soma dos valores da terceira coluna foi de: {terceira_coluna}")
print(f"O maior valor da segunda linha foi: {segunda_linha}")

#print(f"O maior valor da segunda linha foi: {max(matriz[1])}")
# PODERIA ELIMINAR O "PEGAR O MENOR" E SUBSTITUIR POR ISSO 