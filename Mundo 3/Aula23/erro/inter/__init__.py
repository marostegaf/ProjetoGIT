def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: Digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("Entrada de dado interrompida pelo usuário")
            return 0
        else:
            return n

        
def linha(tam = 42):
    return "=" * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[32m{c}\033[m - {item}")
        c += 1
    print(linha())
    opc = leiaInt("\033[32mSua Opção: \033[m")
    return opc
