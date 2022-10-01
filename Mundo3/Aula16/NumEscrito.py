num = ("Zero","Um","Dois","Três","Quatro","Cinco","Seis","Sete","Oito","Nove",
"Dez","Onze","Doze","Treze","Catorze","Quinze","Dezesseis","Dezessete","Dezoito","Dezenove","Vinte")

while True:
    numero_usuario = int(input("Digite um número entre [0, 20]: "))
    if 0 <= numero_usuario <= 20:
        print(f"\nVocê digitou o número {num[numero_usuario]}")
        resp = input("\nDeseja continuar [Sim/Não]: ").strip().upper()[0]
        if resp in "N":
            print("\nObrigado, volte sempre")
            break

    else:
        print("Tente novamente...", end="")
 