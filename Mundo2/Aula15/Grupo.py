homem = 0
maior18 = 0
mulher20 = 0

while True:
    print("="*45)
    print("            CADASTRE UMA PESSOA")
    print("="*45)
    
    idade = int(input("Digite a idade: "))
    sexo = " "
    while sexo not in "MmFf":
        sexo = input("Digite o Sexo [M/F]: ").strip().upper()[0]
    
    if idade >= 18:
        maior18 += 1   
    if sexo in "Ff" and idade <= 20:
        mulher20 += 1  
    if sexo in "Mm":
        homem += 1
    
    print("="*45)
    
    resp = " "
    while resp not in "SsNn":
        resp = input("Quer continuar [S/N]: ").strip().upper()[0]
    if resp in "Nn":
        break

print(f"Maiores de 18 anos: {maior18}")
print(f"Homens: {homem}")
print(f"Mulheres menores de 20 anos: {mulher20}")
