from pprint import pprint # melhora o aspecto de JSON e de dicionários
cursos = []

with open("manipulacao_de_arquivos_csv/dados/cursos.csv", "r", encoding="utf-8") as file:
    for linha in file:
        linguagem, categoria = linha.rstrip().rsplit(",")
        curso = {}
        curso['linguagem'] = linguagem # criando uma chave do dicionário
        curso['categoria'] = categoria # criando outra chave do dicionário
        # ambas indenticas a um JSON
        cursos.append(curso)

pprint(cursos) # printa o dicionário

for curso in cursos:
    print(f"{curso['linguagem']} -> {curso['categoria']}") # outra forma com dicionário