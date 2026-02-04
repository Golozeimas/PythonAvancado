import csv

# 1 - forma de fazer com a biblioteca

# usamos csv.reader para ler os arquivos csv e depois o iteramos com um for

# with open("manipulacao_de_arquivos_csv/dados/cursos.csv","r", encoding="utf-8") as file:
#     leitor = csv.reader(file)
#     for linha in leitor:
#         print(linha)


# 2 - forma feita manualmente, maior manipulação 
# with open("manipulacao_de_arquivos_csv/dados/cursos.csv", "r", encoding="utf-8") as file:
#     for linha in file:
#         linha_atualizada = linha.rstrip().rsplit(",") # traz os dados igual como no uso da biblioteca
#         print(f"Linguagem: {linha_atualizada[0]}, Área de atuação: {linha_atualizada[1]}")
"""
Pega tanto a primeira quanto a segunda coluna
"""

# 3 - forma de leitura mais intuitiva
with open("manipulacao_de_arquivos_csv/dados/cursos.csv", "r", encoding="utf-8") as file:
    for linha in file:
        linguagem, categoria = linha.rstrip().rsplit(",") # como a desecompilação de tuplas
        print(f"{linguagem} -> {categoria}")


# 4 - forma de ordenar a leitura
cursos = []

with open("manipulacao_de_arquivos_csv/dados/cursos.csv", "r", encoding="utf-8") as file:
    for linha in file:
        linguagem, categoria = linha.rstrip().rsplit(",")
        cursos.append(f"{linguagem}-{categoria}")

for curso in sorted(cursos): # ordenado alfabeticamente
    print(curso)