from time import sleep

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

op = 0
while op != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    print("=" * 45)
    op = int(input("Qual é a sua opção: "))
    if op == 1:
        soma = v1 + v2
        print(f"A soma entre {v1} + {v2} é: {soma}")
    
    elif op == 2:
        mult = v1 * v2
        print(f"A multiplicação entre {v1} x {v2} é: {mult}")
    
    elif op == 3:
        if v1 == v2:
            print("Os valores são iguais")
        elif v1 > v2:
            print(f"O valor {v1} é maior que o valor {v2}!")
        else:
            print(f"O valor {v2} é maior que o valor {v1}!")
    
    elif op == 4:
        print("Informe os números novamente")
        v1 = int(input("Digite o primeiro valor: "))
        v2 = int(input("Digite o segundo valor: "))
    
    elif op == 5:
        print("Finalizando...")
    
    else:
        print("Opção inválida")
    
    print("=" * 45)
    sleep(2)
print("Fim do programa")
