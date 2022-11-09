import datetime
ano = int(input("Digite o ano para verificar: "))
if ano == 0:
    ano = datetime.date.today().year
if (ano%4) == 0 and (ano%100) != 0 or (ano%400) == 0:
    print(f"O ano {ano} é BISSEXTO!")
else:
    print(f"O ano {ano} é NORMAL")
