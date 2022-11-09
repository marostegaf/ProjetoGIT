from money import moeda

num = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.red(num,'U$')} é: {moeda.red(moeda.metade(num))}")
print(f"O dobro de {moeda.red(num)} é: {moeda.red(moeda.dobro(num))}")
print(f"Aumentando 10% temos: {moeda.red(moeda.aumentar(num, 10))}")
print(f"Reduzindo 13% temos: {moeda.red(moeda.diminuir(num, 13))}")
