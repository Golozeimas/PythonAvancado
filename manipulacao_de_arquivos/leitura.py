with open("manipulacao_de_arquivos/dados/names.txt", "r", encoding='utf-8') as arquivo: # uso para leitura de um arquivo
    # 1 - forma de leitura
    # print(arquivo.read()) print para vermos no terminal, a leitura das linhas 
    
    # 2 - forma de leitura
    for linha in arquivo:
        print(f"Olá, {linha.rstrip()}") # mais perfomática