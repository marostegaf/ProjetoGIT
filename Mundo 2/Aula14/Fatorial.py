n = int(input("Digite o número para visualizar o seu fatorial: "))
c = n
f = 1

print(f"\033[36m{n}\033[m! = ",end ='')
while c > 0:
    print(c, end="")
    print(" x " if c > 1 else ' = ',end="")
    f *= c
    c -= 1
print(f)

#No discord usando Módulo!
