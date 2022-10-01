total = 0
for i in range(1, 7):
    n = int(input(f"Digite o {i} valor: "))
    if n % 2 == 0:
        total += n
print(f"Soma dos números pares: {total}")
