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

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mDigite um número real válido!\033[m")
        except (KeyboardInterrupt):
            print("Entrada de dado interrompida pelo usuário")
            return 0
        else:
            return n
        


num = leiaInt("Digite um valor: ")
numf = leiaFloat("Digite um número real: ")
print(f"Número inteiro: {num}\nNúmero real: {numf}")
