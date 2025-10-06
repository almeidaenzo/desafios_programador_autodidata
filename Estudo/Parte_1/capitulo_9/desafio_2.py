#Escreva um programa que faça uma pergunta a um usuário e salve a resposta em um arquivo.
nome = input("Digite seu nome: ")

with open("nome.txt", "w") as f:
    f.write(nome)
    
