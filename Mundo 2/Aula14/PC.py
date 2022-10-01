from random import randint

pc = randint(0, 10)
count = 0
acertou = False

while not acertou:
    resp = int(input("Qual número foi o sorteado: "))
    count += 1
    if resp == pc:
        acertou = True
    else:
        if resp < pc:
            print("Mais...")
        else:
            print("Menos...")
print(f"Você acertou o número {pc} e foi preciso de {count} chances!")
