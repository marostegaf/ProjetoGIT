sexo = input("Informe o seu sexo [\033[36mM\033[m/\033[35mF\033[m]: ").strip().upper()[0]
 
while sexo not in "MmFf":
     sexo = input("Dados inválidos. Por favor. Informe o seu sexo: ").strip().upper()[0]

if sexo == "M":
    print("Sexo \033[36mMasculino\033[m registrado com sucesso!")
else:
    print("Sexo \033[35mFeminino\033[m registrado com sucesso!")
