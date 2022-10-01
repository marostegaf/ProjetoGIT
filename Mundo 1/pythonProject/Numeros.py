num = int(input("Digite o número: "))
print(f"Analisando o número: {num}...")
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Milhar: {m}")
print(f"Centena: {c}")
print(f"Dezena : {d}")
print(f"Unidade: {u}")
