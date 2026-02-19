import pandas as pd
import numpy as np


# fazendo os dados para a plalina
dados_aleatorios = {
    "ID":[1,2,3,4,5],
    "Nome":["Matheus", "Ana", "Carla", "Gabriel", "Marcos"],
    "Idade":[20, 19, 18, 17, 16],
    "Cidade":["São paulo", "Rio de janeiro", "Manaus", "Teresina", "São luis"]
}

dados_aleatorios2 = {
    "ID":[6,7,8,9,10],
    "Nome":["João", "Natalia", "Geova", "Marcelo", "Ana clara"],
    "Idade":[20, 30, 19, 13, 14],
    "Cidade":["São paulo", "Rio de janeiro", "Manaus", "Teresina", "São luis"]
}

df_aba1 = pd.DataFrame(dados_aleatorios)
df_aba2 = pd.DataFrame(dados_aleatorios2)

caminho_do_arquivo = "dados_teste/clientes.xlsx"

# assim conseguimos escrever um arquivo excel usando um dataframe como base
# e usando a engine openpyxl
with pd.ExcelWriter(caminho_do_arquivo,engine="openpyxl") as writter:
    # usamos
    df_aba1.to_excel(writter,sheet_name="cliente-1",index=False)
    df_aba2.to_excel(writter, sheet_name="clientes-2", index=False)

print(f"Arquivo excel criado em {caminho_do_arquivo}")

