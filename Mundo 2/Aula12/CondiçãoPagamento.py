import time
prod = float(input("Digite o preço do produto: "))
pag = int(input("Digite a forma de pagamento: "
                "\n1 - Dinheiro/Cheque"
                "\n2 - Cartão"
                "\n3 - 2x no Cartão"
                "\n4 - 3x ou mais no Cartão\n"))
print("\033[35mPROCESSANDO...\033[m")
time.sleep(1)
if pag == 1:
    pag1 = prod - (prod*0.10)
    print(f"10% de desconto aplciado\nPreço a pagar: \033[32m{pag1:.2f}\033[m")
elif pag == 2:
    pag2 = prod - (prod*0.05)
    print(f"5% de desconto aplicado\nPreço a pagar: \033[32m{pag2:.2f}\033[m")
elif pag == 3:
    parcela = prod / 2 
    print(f"Nenhum desconto aplicado\nPreço a pagar: \033[32m{prod:.2f}\033[m / 2x de \033[32m{parcela}\033[m")
elif pag == 4:
    pag4 = prod + (prod*0.20)
    totalparcela = int(input("Quantas parcelas: "))
    parcela = pag4 / totalparcela
    print(f"Juros acrescentado de 20%\nPreço a pagar: \033[32m{pag4:.2f}\033[m / {totalparcela}x de \033[32m{parcela:.2f}\033[m")
else:
    print("\033[31mOpção não existe\033[m")
print("\n\033[32mObrigado\033[m pela compra!")
 