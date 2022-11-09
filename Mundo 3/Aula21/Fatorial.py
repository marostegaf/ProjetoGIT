def fatorial(num=1, show=False):
    """
    --> Calcula o Fatorial de um número.
    num: Número para ser calculado.
    show: (opcional) Mostrar ou não a conta.
    """
    print("=" * 45)
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end="")
            print(" x "if c > 1 else " = ", end="")
        f *= c
    return f


print(fatorial(5, True))
help(fatorial)

"""
def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f*=c
    return f

num = int(input("Fatorial: "))
fat = fatorial(num)
print(f"O fatorial de {num} é: {fat}")
"""