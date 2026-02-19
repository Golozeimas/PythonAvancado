import pandas as pd

# 1 - Importando os dados
# leitura de excel com o pandas
dados_importados = pd.read_excel("dados_teste/clientes.xlsx", sheet_name="clientes-2")

print(dados_importados)

# isso traz um dataframe
print(type(dados_importados))

# 2 - Adicionar coluna como o index
colunas_id_indexada = pd.read_excel("dados_teste/clientes.xlsx", sheet_name="clientes-2",index_col=0)
# retira as coluna que indexam por padrão e coloca a nossa coluna ID para indexar
print(colunas_id_indexada)

# 3 - Importar colunas específicas
importando_colunas_especificas = pd.read_excel("dados_teste/clientes.xlsx", index_col=0, usecols=[1,2])
# vai importar o nome e a idade
print(importando_colunas_especificas)

# 4 - Exportando dados para outra planilha
dados_que_vao_ser_exportados = pd.read_excel("dados_teste/clientes.xlsx", sheet_name="cliente-1")

with pd.ExcelWriter("dados_teste/dados_novos.xlsx",engine="openpyxl") as writter:
    dados_que_vao_ser_exportados.to_excel(writter, sheet_name="Aba-1", index=False)
print("Dados transferidos para outra planilha com sucesso!")