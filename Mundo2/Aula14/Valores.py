n = cont = tot = 0
n = int(input("Digite números inteiros ( [999] para parar ): "))

while n != 999:
    cont += 1
    tot += n
    n = int(input("Digite números inteiros ( [999] para parar ): "))

print("="*45)
print(f"Foram somados \033[35m{cont}\033[m números")
print(f"A soma entres os números foi de: \033[36m{tot}\033[m")
print("="*45)
