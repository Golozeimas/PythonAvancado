import pandas as pd
import os # os faz manipulações do sistema operacional
from pathlib import Path # usa para ver caminho de pastas e arquivos no python

# 1 - Importando todas as páginas das planilhas
sheets_dict = pd.read_excel("dados_teste/clientes.xlsx", sheet_name=None)

pasta_saida_para_dados = "dados_de_manipulacao"

#2 - Se esse caminho não existe, crie para mim a pasta (não cria arquivos)
if not Path.exists(pasta_saida_para_dados):
    os.makedirs(pasta_saida_para_dados)

# 3 - Separando as páginas das planilhas
# usamos o mesmos métodos do dicionário padrão
for nome_aba, tabela in sheets_dict.items():
    # usado para unir arquivos em uma pasta em específico
    caminho_arquivo = os.path.join(pasta_saida_para_dados, f"{nome_aba}.xlsx")
    with pd.ExcelWriter(caminho_arquivo, engine="openpyxl") as writter:
        tabela.to_excel(writter, sheet_name="Aba", index=False)

# 4 - Criando pasta para colocar a planilha com todas as abas
caminho_da_pasta_geral = "dados_de_manipulacao/pasta_de_dados_consolidados"
if not os.path.exists(caminho_da_pasta_geral):
    os.makedirs(caminho_da_pasta_geral)

# garante a criação do arquivo na pasta correta
criacao_do_arquivo_geral = os.path.join(caminho_da_pasta_geral, "clientes.xlsx")

with pd.ExcelWriter(criacao_do_arquivo_geral, engine="openpyxl") as writter:
    for arquivo in Path("dados_de_manipulacao").glob("*.xlsx"):
        tabelas = pd.read_excel(arquivo)
        tabelas.to_excel(writter, sheet_name=arquivo.stem, index=False)