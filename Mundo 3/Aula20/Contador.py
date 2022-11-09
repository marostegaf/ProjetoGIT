from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1

    if p == 0:
        p = 1

    print("=" * 45)
    print(f"Contagem de {i} até {f} indo de {p} em {p}")
    sleep(1.5)

    if i < f:
        for a in range(i, f+1, p):
            print(a, end=" ", flush=True)
            sleep(0.2)
        print("FIM!")
    else:
        for a in range(i, f-1, -p):
            print(a, end=" ", flush=True)
            sleep(0.2)
        print("FIM!")


contador(1, 10, 1)
contador(10, 0, 2)

print("=" * 45)
print("Agora é sua vez de personalizar a contagem: ")
ini = int(input("Início: "))
fim = int(input("Fim:    "))
pas = int(input("Passo:  "))
contador(ini, fim, pas)
