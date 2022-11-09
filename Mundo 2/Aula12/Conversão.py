num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para a conversão: 
1 - Binário
2 - Octal
3 - Hexadecimal''')
op = int(input())
if op == 1:
    print(f"\033[36m{num}\033[m em Binário: \033[32m{bin(num)[2:]}\033[m")
elif op == 2:
    print(f"\033[36m{num}\033[m em Octal: \033[32m{oct(num)[2:]}\033[m")
elif op == 3:
    print(f"\033[36m{num}\033[m em Hexadeciaml: \033[32m{hex(num)[2:]}\033[m")
else:
    print("\033[31mEssa opção não existe\033[m")
