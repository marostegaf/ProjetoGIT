sal = float(input("Digite o salário do funcionário:\n"))
reaj1 = (sal*0.10) + sal
reaj2 = (sal*0.15) + sal
if sal <= 1200:
    print(f"Você recebeu o reajuste de 15% e o seu novo salário vai ser de: {reaj2:.2f}")
else:
    print(f"Você recebeu o reajuste de 10% e o seu novo salário vai ser de: {reaj1:.2f}")
