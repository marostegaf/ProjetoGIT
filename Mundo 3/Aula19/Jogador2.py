time = []
jogo = {}
resultado = []

while True:
    jogo.clear()
    jogo["Jogador"] = input("Nome do Jogador: ")
    jogo["Partidas"] = int(
        input(f"Quantas partidas \033[36m{jogo['Jogador'].upper()}\033[m jogou: "))
    resultado.clear()

    tot = 0
    for i in range(jogo["Partidas"]):
        resultado.append(int(input(f"Quantos Gols na {i+1}ª partida: ")))
        tot += resultado[i]
    jogo["Resultado"] = resultado[:]  # QUANTIDADE DE GOLS POR PARTIDA
    jogo["GOLS"] = sum(resultado)  # TOTAL DE GOLS
    time.append(jogo.copy())

    while True:
        resp = input("Quer continuar [S/N]: ").upper()[0]
        if resp in "SN":
            break
    if resp in "Nn":
        break
print("=" * 55)
print("cod ", end="")
for i in jogo.keys():
    print(f"{i:<15}", end="")
print()
print("=" * 55)
for k, v in enumerate(time):
    print(f"{k:>2}   ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("=" * 55)
while True:
    busca = int(input("Mostrar dados de qual jogador: "))
    if busca == 999:
        break
    if busca >= len(time):
        print()
        print("Esse jogador não existe")
        print()
    else:
        print(
            f" -- LEVANTAMENTO DO JOGADOR: \033[36m{time[busca]['Jogador'].upper()}\033[m")
        for i, g in enumerate(time[busca]["Resultado"]):
            print(f"   - No {i+1}º jogo fez {g} gols")
        print("=" * 55)
print("Continue estudando...")
