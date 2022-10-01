valores = []

for i in range(5):
    valores.append(int(input(f"Digite um valor para {i+1}º posição!: ")))

valoresreais = valores[:]
valoresreais.sort()

print("Valores digitados: ", end="")
for i in range(len(valores)):
    print(f"{i} ", end="")

print(f"\nO maior valor foi: {valoresreais[-1]} e está nas posições: ", end="")
for i, v in enumerate(valores):
    if v == valoresreais[-1]:
        print(f"{i}", end=" ")

print(f"\nO menor valor foi: {valoresreais[0]} e está nas posições: ", end="")
for i, v in enumerate(valores):
    if v == valoresreais[0]:
        print(f"{i}", end="")
 
 # MAIOR E MENOR VALOR, SE HOUVER DOIS NÚMEROS IGUAIS MOSTRAR AS POSIÇÕES TAMBÉM!
