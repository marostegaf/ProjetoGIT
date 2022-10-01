times = (
    "Palmeiras",
    "Fluminense",
    "Flamengo",
    "Corinthians",
    "Internacional",
    "Athletico-PR",
    "Atlético-MG",
    "Santos",
    "América-MG",
    "Bragantino",
    "Goiás",
    "São Paulo",
    "Fortaleza",
    "Botafogo",
    "Ceará SC",
    "Cuiabá",
    "Avaí",
    "Coritiba",
    "Atlético-GO",
    "Juventude",
                )
for t in times:
    print(t)

print(" ")
print(f"Os 5 primeiros colocados são: {times[0:5]}")
print("=" * 115)
print(f"Os 4 ultimos colocados da tabela são: {times[-4:]}")
print("=" * 115)
print(f"Times em ordem alfabética: {sorted(times)}")
print("=" * 115)
print(f"O time do corinthians está na {times.index('Corinthians')+1}ª posição!")
