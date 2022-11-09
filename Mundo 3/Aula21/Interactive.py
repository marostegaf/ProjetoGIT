from time import sleep

c = ('\033[m',
     '\033[36m',
     '\033[0;34;1m',
     '\033[0;31;1m',)


def ajuda(com):
    lin(f"  Acessando o manual do comando \ '{com}' \ ", 1)
    sleep(2)
    print(c[0])
    help(com)
    print(c[0], end="")


def lin(msg, cor=0):
    print(c[cor], end="")
    tam = len(msg) + 4
    print("=" * tam)
    print(msg)
    print("=" * tam)
    print(c[0], end="")


comando = ""
while True:
    lin("  SISTEMA DE AJUDA PyMarostega", 2)
    comando = input("Função ou Biblioteca > \033[33m")
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)

print("\033[31;1m=" * 34)
print("            ATÉ LOGO!")
print("=" * 34)
print(c[0])
