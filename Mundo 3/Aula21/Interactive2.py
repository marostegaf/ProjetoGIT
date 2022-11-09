from time import sleep
from random import randint
c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;46m',
     '\033[0;30;45m',
     '\033[0;30;107m')


def ajuda(com):
    lin(f"  Acessando o manual do comando \ '{com}' \ ", 4)
    sleep(2)
    print(c[6])
    help(com)
    print(c[0], end="")


def lin(msg, cor=0):
    print(c[cor])
    tam = len(msg) + 4
    print("=" * tam)
    print(msg)
    print("=" * tam)
    print(c[0], end="")


comando = ""
while True:
    print(c[2], end="")
    lin("  SISTEMA DE AJUDA PyMarostega", 2)
    print(c[0])
    comando = input("\033[32mFunção ou Biblioteca > \033[m")
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)

lin("  ATÉ LOGO!", 1)
