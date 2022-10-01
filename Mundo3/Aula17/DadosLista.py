num = []

resp = ""
while resp in "Ss":
    num.append(int(input("Digite um número: ")))

    resp = input("Deseja continuar [S/N]: ").upper()[0]

num.sort(reverse=True)
print(f"\nForam digitados {len(num)} números!")
print(f"A lista de forma decrescente é: {num}")
if 5 in num:
    print(f"O valor 5 foi encontrado na {num.index(5)}ª posição!")
else:
    print("O valor 5 não foi digitado")
