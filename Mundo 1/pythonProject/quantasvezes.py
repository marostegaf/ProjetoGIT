nome = input("Digite o seu nome: ").strip().lower()
print(f"A letra A aparece {nome.count('a')} vezes!")
print(f"A primeira letra A apareceu na posição {nome.find('a')+1}")
print(f"A ultima letra A apareceu na posição {nome.rfind('a')+1}")