def lin():
    print("=" * 45)


def area(a, b):
    ter = a * b
    print(f"Área: {ter}m²")


lin()
print(f"={'Controle de Terreno':^42} =")
lin()

l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
area(l, c)
