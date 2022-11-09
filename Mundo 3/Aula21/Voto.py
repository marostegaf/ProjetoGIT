def voto(nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA"
    elif idade < 18 or idade >= 65:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"


nasc = int(input("Ano de nascimento: "))
print(voto(nasc))