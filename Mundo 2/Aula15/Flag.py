s = 0
cont = 0

while True:
    n = int(input("Digite um número: ")) #999 para parar
    if n == 999:
        break
    s += n
    cont += 1

print(f"Foram digitados \033[32m{cont}\033[m números")
print(f"A soma entre eles foi de: \033[32m{s}\033[m")
