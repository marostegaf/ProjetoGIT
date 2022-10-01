from datetime import date
ano = date.today().year
mesy = int(input("Digite o mês do seu nascimento: ")) 
nasc = int(input("Informe sua data de nascimento: "))
idade = ano - nasc
mes = date.today().month
if ano == date.today().year:
    if mes > mesy:
        idade += +1
    else:
        idade += +0

if idade <= 9:
    print("Categoria: \033[36mMIRIM\033[m")
elif idade <= 14:
    print("Categoria \033[36mINFANTIL\033[m")
elif idade <= 19:
    print("Categoria: \033[36mJUNIOR\033[m")
elif idade <= 20:
    print("Categoria: \033[36mSÊNIOR\033[m")
else:
    print("Categoria: \033[36mMASTER\033[m")
