def metade(num = 0, form = False):
    tot = (num / 2)
    return tot if form is False else red(tot)


def dobro(num = 0, form = False):
    tot = (num * 2)
    return tot if form is False else red(tot)


def aumentar(num = 0,p = 0, form = False):
    tot = num + ((num * (p * 0.01)))
    return tot if form is False else red(tot)


def diminuir(num = 0,p = 0, form = False):
    tot = num - (num * (p * 0.01))
    return tot if form == False else red(tot)
    #return tot if format is False else red(num)
    #return tot if not format else red(num)


def red(num = 0, moeda = "R$"):
    return f"{moeda}\033[32m{num:.2f}\033[m".replace(".",",")

def bug(num): # CRIADO PARA CORREÇÃO DE Bug
    """
    --> Criado para correção de Bug
    """
    return red(num)

def resumo(num = 0, aum = 10, red = 5   ):
    print("=" * 35)
    print("RESUMO DO VALOR".center(34))
    print("=" * 35)
    print(f"Preço Analisado: \t{bug(num)}")
    print(f"Dobro do preço: \t{dobro(num, True)}")
    print(f"Metade do preço: \t{metade(num, True)}")
    print(f"{aum}% de aumento: \t{aumentar(num, aum, True)}")
    print(f"{red}% de redução: \t\t{diminuir(num, red, True)}")
    print("=" * 35)
