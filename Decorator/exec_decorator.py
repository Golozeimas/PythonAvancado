from decorador import my_decorator, uppecaser_palavras, split_string

@my_decorator # modifica sem alterar o código diretamente no principal
def oi():
    print("oi")

oi()

@uppecaser_palavras
def palavras():
    # usamos o return para transformar essas palavras
    # o print era usado como print
    return "Essas palavras vão ser maiusculas" 

print(palavras())

@split_string
@uppecaser_palavras # dá pra usar um encima do outro diretamente
def palavras_cortadas_por_virgula():
    return "Adele,eminem,kanye west,nas,tyler"

print(palavras_cortadas_por_virgula())
