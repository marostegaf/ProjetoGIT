n1 = int(input("Digite o primeiro termo da PA: "))
n2 = int(input("Digite a razão da PA: "))

termo = n1
cont = 0 
resp = True

while cont < 10:
    print(termo, end='')
    print(" " if cont < 9 else '', end='')
    termo += n2
    cont += 1

while resp == True:
    voce = input("\nDeseja continuar? [\033[32mSim\033[m/\033[31mNão\033[m]\n").strip().upper()[0]
    if voce == "S":
        voced = int(input("Deseja visualizar quantos termos: "))

        while not voced == 0:
            print(termo, end=' ')
            print(", " if cont < 9 else '', end='')
            termo += n2
            voced -= 1
            cont += 1
    else:
        resp = False
        print("\033[35mObrigado, volte sempre!\033[m")
print(cont)
