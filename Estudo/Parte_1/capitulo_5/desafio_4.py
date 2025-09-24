#Escreva um programa que permita que o usuário pergunte sua altura, cor favorita
#ou autor favorito e retorne o resultado a partir do dicionário criado no desafio anterior.

atributos = {
    "altura":"1.77",
    "cor":"verde",
    "banda":"angra"   
}

pergunta = input("Digite sua altura, cor favorita e banda favorita")
if pergunta in atributos:
    resposta = atributos[pergunta]
    print(resposta)