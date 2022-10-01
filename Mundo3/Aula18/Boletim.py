ficha = []

while True:
    nome = input("Nome: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    med = (n1+n2)/2
    ficha.append([nome, [n1, n2], med])

    resp = input("Deseja continuar [S/N]: ").upper()[0]
    if resp in "N":
        break

print()
print("=" * 30)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print("=" * 25)
for i,a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    print("=" * 50)
    opc = int(input("Deseja visualizar a nota de qual aluno: "))
    if opc == 999:
        print("Finalizando...")
    if opc <= len(ficha) - 1:
        print(f"Notas: {ficha[opc][0]} são: {ficha[opc][1]}")
