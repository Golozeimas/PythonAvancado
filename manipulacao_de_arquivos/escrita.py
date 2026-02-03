name = input("Escreva o nome do aluno: ")

"""
Modos para operações em arquivos - 

W -> modo write (escrita do arquivo)

A -> modo append (escrita mas adiciona apenas no final)

R -> modo read (leitura dos dados do arquivo)

"""

# implementação - 1

# arquivo = open("manipulacao_de_arquivos/dados/names.txt", "w") estou passando para escrever esse arquivo

# arquivo = open("manipulacao_de_arquivos/dados/names.txt", "a", encoding="utf-8") # aqui é para escrever e salvar  
                                                                                   # encoding resolve o problema do acentos
# arquivo.write(f"{name}\n")  sempre desce um nível pós escrita

# arquivo.close()  fecha o arquivo por questão de desempenho

# implementação - 2 (mais utilizada e rápida)

with open("manipulacao_de_arquivos/dados/names.txt","a",encoding="utf-8") as arquivo:
    arquivo.write(f"{name}\n") # usamos a mesma coisa, só não precisamos fechar, pq já fecha sozinho
                               # o próprio python ajuda a fechar a função quando não mais usada
