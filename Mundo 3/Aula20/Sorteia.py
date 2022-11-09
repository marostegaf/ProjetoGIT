from operator import xor
from random import randint
from time import sleep

sorteio = []
def sorteia():
    par = 0
    print("Números sorteados: ",end="")
    for i in range(5):
        sorteio.append(randint(1, 10))
        print(sorteio[i],end=" ",flush=True)
        sleep(0.4)

def somapar():
    par = 0
    for valor in sorteio:
        if valor % 2 == 0:
            par += valor
    print(f"\nSomando os valores pares de {sorteio} temos: {par}")

sorteia()
somapar()