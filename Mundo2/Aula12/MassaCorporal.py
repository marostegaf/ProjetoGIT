peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso/(altura ** 2)
print(f"IMC: {imc:.2f}")
if imc < 18:
    print("\033[33mAbaixo do peso\033[m")
elif imc >= 18 and imc <= 25:
    print("\033[32mPeso ideal\033[m")
elif imc >= 25.1 and imc <= 30:
    print("\033[34mSobrepeso\033[m")
elif imc >= 30.1 and imc <= 40:
    print("\033[31mObesidade\033[m")
else:
    print("\033[30mObesidade mórbida\033[m")
