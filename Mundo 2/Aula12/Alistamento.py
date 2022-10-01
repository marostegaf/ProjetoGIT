from datetime import date
anoatual = date.today().year
nasc = int(input("Digite o ano do seu nascimento: "))
idade = anoatual - nasc
if idade <= 15:
    saldo = 18 - idade
    novo = anoatual + saldo
    print(f"Não se preocupe seu alistamento ainda está longe! \033[36m{saldo}\033[m anos / \033[36m{novo}\033[m")
elif idade == 16:
    seis = anoatual + 2
    print(f"Seu alistamento ainda não é Obrigatório, será no ano de:  \033[32m{seis}\033[m")
elif idade == 17:
    deze = anoatual + 1
    print(f"Seu alistamento ainda não é Obrigatório, será no ano de: \033[32m{deze}\033[m")
elif idade == 18:
    print(f"Seu alistamento é obrigatório esse ano! \033[32m{anoatual}\033[m")
elif idade == 19:
    nove = anoatual - 1
    print(f"Seu alistamento está atrasado a um ano, foi no ano de: \033[31m{nove}\033[m")
elif idade == 20:
    vinte = anoatual - 2
    print(f"Seu alistamento está atrasado dois anos, foi no ano de: \033[31m{vinte}\033[m")
else:
    saldo = idade - 18
    antigo = anoatual - saldo
    print(f"Seu alistamento está atrasado há muito tempo, \033[31m{saldo}\033[m anos / \033[31m{antigo}\033[m")

#saldo = 18 - idade / idade - 18
