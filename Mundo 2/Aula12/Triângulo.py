a = float(input("Digite a primeira medida: "))
b = float(input("Digite a segunda medida: "))
c = float(input("Digite a terceira medida: "))

if a + b > c and a + c > b and b + c > a:
    print("\033[32mEssas medidas formam um triângulo\033[m")
    if a == b and b == c :
        print("\n\033[33mTriângulo:\033[m \033[32mEquilátero\033[m")
    elif a == b or a == c or b == c:
        print("\n\033[33mTriângulo:\033[m \033[32mIsósceles\033[m")
    else:
        # Ou para calcular o ESCALENO / a != b or b != c or c != a
        print("\n\033[33mTriângulo:\033[m \033[32mEscaleno\033[4m")
else:
    print("\033[31mEssas medidas não formam um triângulo\033[m")
