mult = 1
while True:
    print("="*45)
    n = int(input("Digite um valor para ver a tabuada: ")) #Negativo para parar
    print("="*45)
    
    if n < 0:
        break
    while mult < 11:
        tot = n * mult
        print(f"{n} x {mult} = \033[36m{tot}\033[m") # N * MULT = ( N*MULT ) (Sem usar o TOT)
        mult += 1
    mult = 1

print("\033[35mVolte sempre!\033[m")
