from random import randint

you = int(input("Escolha entre:\n1 - Pedra\n2 - Papel\n3 - Tesoura\n"))
pc = randint(0,2) # 0 = Pedra / 1 = Papel / 2 = Tesoura

if you == 1:
    if pc == 0:
        print("Pedra \033[33mvs\033[m Pedra: \033[36mEmpate\033[m")
    elif pc == 1:
        print("Pedra \033[33mvs\033[m Papel: \033[31mVocê perdeu\033[m")
    else:
        print("Pedra \033[33mvs\033[m Tesoura: \033[32mVocê ganhou\033[m")
elif you == 2:
    if pc == 0:
        print("Papel \033[33mvs\033[m Pedra: \033[32mVocê ganhou\033[m")
    elif pc == 1:
        print("Papel \033[33mvs\033[m Papel: \033[36mEmpate\033[m")
    else:
        print("Papel \033[33mvs\033[m Tesoura: \033[31mVocê perdeu\033[m")
elif you == 3:
    if pc == 0:
        print("Tesoura \033[33mvs\033[m Pedra: \033[31mVocê perdeu\033[m")
    elif pc == 1:
        print("Tesoura \033[33mvs\033[m Papel: \033[32mVocê ganhou\033[m")
    else:
        print("Tesoura \033[33mvs\033[m Tesoura: \033[36mEmpate\033[m")
else:
    print("\033[31mEssa opção não existe\033[m\nTente da próxima vez...")
