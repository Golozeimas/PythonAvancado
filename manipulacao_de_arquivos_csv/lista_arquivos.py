import glob, os, zipfile

# 1 - pega o diretório atual
print(os.getcwd())

# 2 - listar todos os arquivos .txt da pasta dados_teste
for linha_txt in glob.glob("dados_teste/*.txt"):
    print(linha_txt)

# 3 - listar todos os arquivos .csv da pasta dados_teste
for linha_csv in glob.glob("dados_teste/*.csv"):
    print(linha_csv)

# 4 - zipar todos os arquivos da pasta dados_teste, misturando glob com zip file

# pega a lista de todos os arquivos
todos_os_arquivos = glob.glob("dados_teste/*")

# mesmo processo de criação e leitura de arquivos com exceção de se tratar de um zip
with zipfile.ZipFile("dados_teste/dados.zip","w") as zipf: # o caminho do seu zip e a forma no caso (escrita)
    for arquivo in todos_os_arquivos: # pegando todos os arquivos
        zipf.write(arquivo) # escreve no arquivo zipado todos arquivos dentro de dados_teste