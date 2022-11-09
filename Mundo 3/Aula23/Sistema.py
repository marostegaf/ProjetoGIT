from erro.menu import *
from erro.inter import *
from time import sleep

arq = "a.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar uma nova pessoas", "Sair do sistema"])
    if resposta == 1:
        #Opção de listar o conteúdo de um aarquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa
        cabeçalho("NOVO CADASTRO")
        nome = input("Nome: ")
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #Opção de sair do programa
        cabeçalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[31mERRO: Digite uma opção válida!\033[m")  
    sleep(2)           
 