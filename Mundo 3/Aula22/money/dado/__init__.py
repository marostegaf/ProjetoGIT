def leiaDin(msg):
    val = False
    while not val:
        entrada = input(msg).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f"ERRO: {entrada} é um preço inválido!")
        else:
            val = True
            return float(entrada)

def leiaint(msg):
    num = ""
    while True:
        num = input(msg)
        if num.isnumeric():
            break
        else:
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")
    return num
    