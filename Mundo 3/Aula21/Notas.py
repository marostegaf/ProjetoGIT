def notas(*num, sit=False):
    """
    --> Analisar notas e situações de alunos.
    n: Nota dos alunos
    sit: (opcional), indica se deve ou não mostrar a situação dos alunos.
    return: dicionário com informações dos alunos
    """
    print("=" * 45)
    notas = {}
    notas["total"] = len(num)
    notas["maior"] = max(num)
    notas["menor"] = min(num)
    notas["média"] = sum(num)/len(num)
    if sit:
        if notas["média"] >= 7:
            notas["situação"] = "BOA"
        elif notas["média"] >= 5:
            notas["situação"] = "RAZOAVEL"
        else:
            notas["situação"] = "RUIM"

    #for i,j in notas.items():
    #    print(f"{i} = {j}")
    return notas


resp = notas(9, 10, 5.5, 2.5, 8.5, sit = True)
print(resp)
