'''
'r' -> Usado somente para ler algo
'w' -> Usado somente para escrever algo
'r+' -> Usado para ler e escrever algo
'a' -> Usado par acrescentar algo

'''

'''
with open("valores.txt","w") as arquivo:
    arquivo.write("Mensagem" + "\n") # irá escrever a mensagem e pular uma linha

Se o arquivo não existir ele vai criar e se o arquivo já existir ele vai substituir 
'''

'''
with open("valores.txt", "a") as arquivo:
    arquivo.write("Mensagem" + "\n") 

Irá fazer a mesma coisa que o de cime porém ele irá adicionar ao final do arquivo
e não irá substituir
'''

'''
with open("valores.txt","r") as arquivo:
    for linha in arquivo:
        print(linha) # pode colocar um end = "" no final para ele não pular uma linha

Irá ler o arquivo
'''

'''
with open("valores.txt","r+") as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.write("Mensagem") 

Irá ler o arquivo e no final escrever a mensagem
'''
