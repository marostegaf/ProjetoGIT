from audioop import reverse
from random import randint
from time import sleep
from operator import itemgetter

jogo = {"Jogador 1": randint(1, 6),
        "Jogador 2": randint(1, 6),
        "Jogador 3": randint(1, 6),
        "Jogador 4": randint(1, 6)}

ranking = []
for i, j in jogo.items():
    print(f"O {i} tirou: {j}")
    sleep(0.5)
#FUNÇÃO IMPORTANTE
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(f"\n{'RANKING':^34}")
for i, j in enumerate(ranking):
    print(f" - {i+1}º lugar: {j[0]} com {j[1]}")
