import csv

cursos = []
with open("manipulacao_de_arquivos_csv/dados/cursos.csv", "r", encoding="utf-8")as file:
    reader = csv.DictReader(file)
    for linha in reader:
        print(linha) # já transforma em dicionários
        
        # caso queira adicionar em uma lista
        cursos.append({
            "language":linha['language'],
            "category":linha['category']
        }) # adição das chaves pós parênteses para indicar que se trata de um dicionário

print(cursos)