n1 = int(input("Digite o primeiro termo da PA: "))
n2 = float(input("Qual a razão dessa PA: "))
count = 0

while count < 10:
    tot = n1 + n2 * count
    count += 1
    if count % 2 == 0:
        print(f"\033[35m{tot}\033[m",end='')
        print(", " if count < 9 else '',end='')
    else:
        print(f"\033[36m{tot}\033[m",end='')
        print(", " if count < 9 else '',end='')
