                                        #Módulos

#exemplo - import [nome do módulo]
#sintaxe para usar o módulo: [nome do módulo](nome do módulo importado).[código](função ou variável desejada)
import math

math.pow(2, 3) #.pow(x, y) x é elevado à potência y


import random

random.randint(0, 1000) #.randint(x, y) gera números inteiros aleatórios de x à y


import statistics #usado para calcular a média, a mediana e a moda em um iterável de números

numeros = [1, 5, 33, 12, 46, 33, 2]

#média
print(statistics.mean(numeros))

#mediana
print(statistics.median(numeros))

#moda
print(statistics.mode(numeros))


import keyword #usado para verificar se uma string é uma palavra-chave do python
print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))
print(keyword.iskeyword("True"))
print(keyword.iskeyword("teste"))




