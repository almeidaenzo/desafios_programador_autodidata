#Escreva uma função que converta uma string em um float e retorne o resultado.
#Use a manipulação de exceções para capturar a exceção que pode ocorrer.


def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Não é possível converter")

a = convert("20")
print(a)