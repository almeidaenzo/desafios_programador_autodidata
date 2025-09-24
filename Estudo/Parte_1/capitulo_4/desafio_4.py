#Escreva um programa com duas funções. A primeira função deve receber um 
#inteiro como parâmetro e retornar o resultado do inteiro dividido por 2. A segunda 
#função deve receber um inteiro como parâmetro e retornar o resultado do inteiro 
#multiplicado por 4. Chame a primeira função, salve o resultado como uma variável e passe-a como parâmetro para a segunda função.

def funcao_1(x):
    return x / 2

def funcao_2(x):
    return x * 4

y = funcao_1(4)
z = funcao_2(y)

print(z)