from random import randint

num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

'''
menor = maior = num[0]
for i in range(5):
    if num[i]< menor:
        menor = num[i]
for i in range(5):
    if num[i] > maior:
        maior = num[i]

COM O JEITO LÓGICO SEM USAR O " MAX " E O " MIN " !
'''
print("Os valores sorteados foram: ",end="")
for i in num:
    print(f"{i} ",end="")

print(f"\nMaior valor sorteado: {max(num)}")
print(f"Menor valor sorteado:{min(num)}")
