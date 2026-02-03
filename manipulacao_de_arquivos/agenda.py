import os

def adiciona_contato():
    nome = input("nome do contato:")
    idade = int(input("idade do contato:"))
    telefone = input("telefone do contato:")

    with open("manipulacao_de_arquivos/dados/contatos.txt","a",encoding="utf-8") as arquivo:
        arquivo.write(f"nome: {nome.strip()}, idade: {idade} e telefone: {telefone.strip()}")
        return

def listar_contatos():
    with open("manipulacao_de_arquivos/dados/contatos.txt","r",encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha)
            os.system("pause")

def excluir_contatos():
    with open("manipulacao_de_arquivos/dados/contatos.txt","w",encoding="utf-8") as arquivo:
        arquivo.write("") 

def main():
    temp = True
    while temp:
        print("=" * 10,"Agenda de contatos", "=" * 10)
        print("1 - adicionar contatos")
        print("2 - listar contatos")
        print("3 - excluir contatos")
        print("4 - sair")
        escolha = int(input("Digite qual operação deseja fazer:\n"))
    
        if escolha == 1:
            adiciona_contato()
        if escolha == 2:
            listar_contatos()
        if escolha == 3:
            excluir_contatos()
            print("Todos os contatos foram excluidos!")
            os.system("pause")
        if escolha == 4:
            temp = False

main()