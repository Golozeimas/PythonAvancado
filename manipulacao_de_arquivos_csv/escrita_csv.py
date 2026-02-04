import csv

linguagem_de_programacao = input("Informe a linguagem de programação: ")
categoria_da_linguagem = input("Informe a categoria da mesma: ")

# uma das formas

# no caso de dupla lista fazemos uma lista de listas para o csv entender

# dados = [
#     ["linguagem","categoria"],
#     [linguagem_de_programacao,categoria_da_linguagem]
# ]
# with open("manipulacao_de_arquivos_csv/dados/cursos_pt2.csv","a",encoding="utf-8") as file:
#     # passa o arquivo, e determina ao final da linha o que fazer, no caso '\n' para descer uma linha
#     writer = csv.writer(file, lineterminator="\n")
#     writer.writerows(dados)

# outra forma
with open("manipulacao_de_arquivos_csv/dados/cursos_pt2.csv", "a", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo, lineterminator="\n")
    writer.writerow([linguagem_de_programacao,categoria_da_linguagem])