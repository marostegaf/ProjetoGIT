import time
from random import randint
a = randint(1, 10)
#print("-=-" * 20)
resp = int(input("Digite um número aleátorio de 1 a 10 e tente acertar: "))
print("\033[35mPROCESSANDO...\033[m")

time.sleep(1) # Esperar 1 segundo
if resp == a:
    print(f"\033[32mParabéns\033[m, você acertou o número sorteado: \033[36m{a}\033[m")
else:
    print(f"\033[31mVocê errou\033[m, Tente da próxima vez, o número sorteado foi: \033[36m{a}\033[m")
