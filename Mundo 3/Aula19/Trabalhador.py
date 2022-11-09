from datetime import date
ano = date.today().year

trabalho = {}

trabalho["Nome"] = input("Nome: ")
nasc = int(input("Ano de nascimento: "))
idade = ano - nasc
trabalho["Idade"] = idade
trabalho["CTPS"] = int(input("Carteira de trabalho: "))

if trabalho["CTPS"] != 0:
    trabalho["Ano de Contratação"] = int(input("Ano de Contratação: "))
    trabalho["Salário"] = float(input("Digite o salário: "))
    trabalho["Aposentadoria"] = trabalho["Idade"] + ((trabalho["Ano de Contratação"]) + 35) - ano

print("=" * 45)
for i, j in trabalho.items():
    print(f"- {i} é igual a {j}")
