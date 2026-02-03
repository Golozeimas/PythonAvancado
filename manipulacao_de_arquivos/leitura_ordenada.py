names = []

with open("manipulacao_de_arquivos/dados/names.txt", "r", encoding='utf-8') as arquivo:
    for linha in arquivo:
        names.append(linha.strip())
    names.sort()
    for l in names:
        print(l)