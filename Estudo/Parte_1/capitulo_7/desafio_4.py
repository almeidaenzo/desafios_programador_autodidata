# Escreva um programa com um loop infinito (com a opção de digitar q para sair) e uma lista de números.
# A cada iteração do loop, peça ao usuário para fornecer um número da lista e informe se o seu palpite estava ou não correto

lista = [2, 4, 6, 7]
while True:
    a = input("Pressione 'q' para sair ou tente adivinhar o número: ")
    if a == "q":
        break
    
    try:
        a = int(a)
    except ValueError:
        print("Digite um númeor ou q para sair")
    if a in lista:
        print("Você acertou um número")
    else:
        print("Você errou")
