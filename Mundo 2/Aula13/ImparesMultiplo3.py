impar = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += 1
        impar += i
print(f"Foram somados {cont} números e o total foi: {impar}")
