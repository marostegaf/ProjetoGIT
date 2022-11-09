jogo = {}
resultado = []

jogo["Jogador"] = input("Nome do Jogador: ")
jogo["Partidas"] = int(input(f"Quantas partidas {jogo['Jogador']} jogou: "))

tot = 0
for i in range(jogo["Partidas"]):
    resultado.append(int(input(f"Quantos Gols na {i+1}ª partida: ")))
    tot += resultado[i]
jogo["Resultado"] = resultado[:] # QUANTIDADE DE GOLS POR PARTIDA
jogo["GOLS"] = sum(resultado) # TOTAL DE GOLS

print(
    f"O jogador \033[36m{jogo['Jogador']}\033[m jogou {jogo['Partidas']} partidas")
print("=" * 45)

for i, v in enumerate(jogo["Resultado"]):
    print(f"= Na \033[36m{i+1}\33[mª partida fez {v} gols {'=':>18}")
print("=" * 45)
print(f"Foram {jogo['GOLS']} gols no total")
