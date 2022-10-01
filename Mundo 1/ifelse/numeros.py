a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
# VERIFICANDO O MAIOR
if a > b and a > c:
    print(f"O número maior é o primeiro: {a}")
elif b > c:
    print(f"O número maior é o segundo: {b}")
else:
    print(f"O número maior é o terceiro: {c}")
# VERIFICANDO O MENOR
if a < b and a < c:
    print(f"O número menor é o primeiro: {a}")
elif b < c:
    print(f"O número menor é o segundo: {b}")
else:
    print(f"O número menor é o terceiro: {c}")
