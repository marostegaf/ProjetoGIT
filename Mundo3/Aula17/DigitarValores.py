valores = []

resp = ""
while resp in "Ss":
    resp_usuario = int(input("Digite um valor: "))
    if resp_usuario not in valores:
        print(f"Valor {resp_usuario} adicionado com sucesso")
        valores.append(resp_usuario)
    
    else:
        print("Esse número já existe")

    resp = input("Deseja continuar? [SIM/NÃO]: ").upper()[0]
 
valores.sort()
print("\nValores: ",end="")
for i in range(len(valores)):
    print(f"{valores[i]}",end=" ")
