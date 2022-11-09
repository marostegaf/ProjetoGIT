def ficha(jog="<desconhecido>", gols=0):
    print(f"O {jog} marcou {gols} gols no campeonato.")


jogador = input("Digite o nome do jogador: ")
gol = input(f"Quantos gols {jogador} marcou: ")
if not gol.isnumeric():
    gol = 0

if jogador.strip() == "":
    ficha(gols=gol)
else:
    ficha(jogador, gol)

"""def ficha(jog="<desconhecido>",gol=0):
    print(f"O jogador {jog} fez {gol} gols no campeonato")



n = input("Nome do Jogador: ")
g = input("Número de gols: ")

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == "":
    ficha(gol=g)
else:
    ficha(n, g)"""
