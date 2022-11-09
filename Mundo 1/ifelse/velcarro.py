vel = float(input("Digite a velocidade: "))
if vel > 80:
    multa = (vel - 80) * 7
    print(f"Você ultrapassou a velocidade permitida e receberá uma multa de: \033[31mR${multa:.2f}")
else:
    print("Parabéns você está na velocidade permitida de \033[32m80km/h!")