frase = input("Digite uma frase: ")
cont = len(frase)
pa = False
for i in range(cont):
    if frase == frase[::-1]:
        pa = True
    
if pa == True:
    print(f'A frase " {frase.title()} " é um \033[32mPALINDROMO!\033[m')
else:
    print(f'A frase " {frase.title()} " não é um \033[31mPALINDROMO\033[m')


'''
frase = input("Digite uma frase: ").strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'A frase " {frase.capitalize()} " é um \033[32mPALINDROMO!\033[m')
else:
    print(f'A frase " {frase.capitalize()} " não é um \033[31mPALINDROMO\033[m')
'''