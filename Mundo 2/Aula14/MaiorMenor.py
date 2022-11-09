resp = "S"
soma = quant = med = maior = menor = 0
while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = input("Quer continuar [S/N]: ").upper().strip()[0]
med = soma / quant

print(f"Você digitou {quant} números e a média foi: {med:.2f}")
print(f"O maior valor foi: {maior}\nO menor valor foi: {menor}")
