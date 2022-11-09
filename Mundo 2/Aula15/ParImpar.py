from random import randint

win = 0
while True:
    n = int(input("Digite um valor: "))
    pc = randint(0, 10)
    #print(pc)
    resp = " " #Importante colocar esse "Espaço"
    while resp not in "PpIi":
        resp = input("Você deseja jogar Par ou Impar [P/I]: ").strip().upper()[0]
    
    tot = n + pc
    print(f"{n} + {pc} = {tot}")
    
    if tot % 2 == 0 and resp in "Pp":
        print("\033[32mParabéns você ganhou\033[m")
        win += 1
    if tot % 2 == 0 and resp in "Ii":
        print("\033[31mVocê perdeu\033[m")
        break
    if tot % 2 != 0 and resp in "Pp":
        print("\033[31mVocê perdeu\033[m")
        break
    if tot % 2 != 0 and resp in "Ii":
        print("\033[32mParabéns você ganhou\033[m")
        win += 1

print("="*45)
print("                FIM DE JOGO")
print(f"            Você ganhou \033[32m{win}\033[m vezes")
print("="*45)
