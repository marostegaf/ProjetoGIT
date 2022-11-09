from money import moeda

num = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.red(num)} é: {moeda.metade(num, True)}")
print(f"O dobro de {moeda.red(num)} é: {moeda.dobro(num, True)}")
print(f"Aumentando 10% temos: {moeda.aumentar(num, 10, True)}")
print(f"Reduzindo 13% temos: {moeda.diminuir(num, 13, True)}")
