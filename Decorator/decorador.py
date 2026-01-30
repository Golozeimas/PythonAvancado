
def my_decorator(funcao):
    # wrapper é usado como default
    def wrapper():
        print("Antes da função")
        funcao()
        print("Depois da função")
    return wrapper


def uppecaser_palavras(func):
    def wrapper():
        funcao = func()
        letras_maiusculas = funcao.upper()
        return letras_maiusculas
    return wrapper

def split_string(func):
    def wrapper():
        funcao_dividida = func()
        palavras_divididas = funcao_dividida.split(",")
        return palavras_divididas
    return wrapper

