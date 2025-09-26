#LOOPS

                                        #Loops For
#loop usado para percorrer um iterável.
#exemplo com uma string
nome = "Enzo"
for n in nome:
    print(n)

#exemplo com uma lista
lista = ["01", "02", "03", "04"]

for i in lista:
    print(i)

#exemplo com uma tupla
bandas = ("Iron Maiden", "Megadeth", "Angra", "Rapsody")
for banda in bandas:
    print(banda)

#exemplo com um dicionário
atributos = {
    "altura":"178",
    "peso":"87",
    "idade":"22"
}
for atributo in atributos:
    print(atributo)

#usando loops para alterar itens de uma lista
carro = ["motor",
         "pneus",
         "rodas",
         "volante"]
i = 0 #variável de índice, representa um índice de um iterável(uma lista, nesse caso). A variável começa em 0, pois i=0, e é incrementada sempre que o loop itera
for itens in carro: #itera pela lista
    novo = carro[i] #variável que contém o item atual da lista
    novo = novo.upper()
    carro[i] = novo #substiui o índice pelo que tem no método upper()
    i += 1 #incrementa i para procurar o item seguinte da lista
print(carro)

#outra forma
carro = ["motor",
         "pneus",
         "rodas",
         "volante"]
for i, itens in enumerate(carro):
    novo = carro[i]
    novo = novo.upper()
    carro[i] = novo
print(carro)

#loops sendo usados para pegar todas as strings de duas listas diferentes,
#deixando os caracteres maiúsculos e inserindo em uma nova lista

motos = ["CB1000", "CBR1000", "R1", "Ninja 650"]
carros = ["Mustang", "Supra", "Miata", "Impala"]
nova_lista = []

for veiculos in motos:
    veiculos = veiculos.upper()
    nova_lista.append(veiculos)

for veiculos in carros:
    veiculos = veiculos.upper()
    nova_lista.append(veiculos)
print(nova_lista)

                                        #Função Range
#Usado para criar uma sequência de inteiros e empregar um loop for para percorrer
# recebe dois parâmetros: o número onde a sequência começa e onde acaba

for i in range(1, 11):
    print(i)                                        

                                        #While
#executa um código enquanto uma condição é avaliada como True

# x = 10
# while x > 0:
#     print('{}'.format(x))
#     x -= 1
# print("Feliz Ano Novo")

# #exemplo caso o loop seja sempre True:

# while True:
#     print("Loop infinito")

                                        #Instrução Break
#a instrução com a palavra-chave break serve para encerrar um loop

for i in range(0, 101):
    print(i)
    break

#exemplo com entrada de usuário

# perguntas = [
#     "Qual seu nome?     ",
#     "Qual sua idade?    ",
#     "Qual sua pergunta?     "
# ]
# n = 0
# while True:
#     print("Digite 'Q' para sair")
#     a = input(perguntas[n])
#     if a == "q":
#         break
#     n = (n + 1) % 3

                                            #Instrução Continue
#usa-se para interromper a iteração atual de um loop e passar para a próxima iteração
# exemplo: exibir todos os números de 1 a 5, exceto o 3

for i in range(1,6):
    if i == 3:
        continue
    print(i)

#usando o loop while com continue:

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

                                        #Loops aninhados
#é possível ter um loop dentro de outro loop, que estaria dentro de um loop existente
# em outro loop, que faria parte de ainda outro loop
# Não há limites para o número de loops, embora seja recomendável limitar isso
# o loop que tem em outro loop chama-se loop externo
# o loop aninhado chama-se loop interno
# quando tiver un loop aninhado, o loop interno percorrerá seu iterável uma vez para cada iteração do loop externo

for i in range(1, 4):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)                                          

#usando dois loops for para somar cada número de uma lista com todos os números de outra lista
lista_1 = [1, 2, 3]
lista_2 = [1, 2, 3]
lista_soma = []

for i in lista_1:
    for j in lista_2:
        lista_soma.append(i + j)

print(lista_soma)