print("="*45)
print(f"{'BANCO MAROSTEGA':^43}")
print("="*45)

valor = int(input("Que valor você deseja sacar: R$\033[32m"))
print(f"\033[m",end ="")
total = valor

ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de \033[32m{totced}\033[m cédulas de R$\033[32m{ced:.2f}\033[m")
        if ced == 100:
            ced = 50
        
        elif ced == 50:
            ced = 20
        
        elif ced == 20:
            ced = 10

        elif ced == 10:
            ced = 5

        elif ced == 5:
            ced = 2
        
        elif ced == 2:
            ced = 1

        totced = 0
        if total == 0:
            break
