num = [] 
par = []
impar = []

resp = ""
while resp in "Ss":
    n = int(input("Digite um valor: "))
    num.append(n)

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    resp = input("Deseja continuar [S/N]: ").upper()[0]

print(f"Todos os valores: {num}")
print(f"Valores pares: {par}")
print(f"Valores impares: {impar}")
