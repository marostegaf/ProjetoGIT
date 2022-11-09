viagem = float(input("Qual a distãncia da viagem em KM: "))
valor1 = viagem * 0.50
valor2 = viagem * 0.45
if viagem <= 200:
    print(f"Sua viagem custará: R${valor1:.2f}")
else:
    print(f"Sua viagem custará: R${valor2:.2f}")
