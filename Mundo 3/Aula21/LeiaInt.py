def leiaint(msg):
    num = ""
    while True:
        num = input(msg)
        if num.isnumeric():
            break
        else:
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")
    return num


num = leiaint("Digite um número: ")
print(f"\033[32mVocê digitou o número: {num}\033[m")


"""def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")

        if ok:
            break
    return valor
    """