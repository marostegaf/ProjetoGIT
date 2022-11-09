a = float(input("Digite o primeiro comprimento: "))
b = float(input("Digite o segundo comprimento: "))
c = float(input("Digite o terceiro comprimento: "))
if a + b > c and a + c > b and b + c > a:
    print("Parabéns, essas medidas formam um triângulo!")
else:
    print("Essas medidas não formam um triângulo!")