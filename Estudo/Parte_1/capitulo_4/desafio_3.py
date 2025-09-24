#Escreva uma função que receba três parâmetros obrigatórios e dois parâmetros opcionais.

def parametros(a, b, c, d=5, e=3):
    return a + b * c + d / 3

resultado = parametros(10, 3, 4)

print(resultado)
