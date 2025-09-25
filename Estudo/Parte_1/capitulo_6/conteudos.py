#MANIPULAÇÃO DE STRINGS

                                        #Strings com aspas triplas
#Se a string se estender por mais de uma linha, insere-se aspas triplas.

print("""
      linha um
      linha dois
      linha três
      linha quatro
""")

                                        #Índices
#strings são iteráveis. É possível procurar cada caractere de uma string através de um índice.
#primeiro caractere, assim como outros iteráveis, será índice 0

exemplo = "Angra"
print(exemplo[0])
print(exemplo[1])
print(exemplo[2])
print(exemplo[3])
print(exemplo[4])

#o python também permite índices negativos, o que faz buscar da direita para a esquerda
#índice -1 traz o último índice
exemplo = "Angra"
print(exemplo[-5])
print(exemplo[-4])
print(exemplo[-3])
print(exemplo[-2])
print(exemplo[-1])

exemplo = "Angra"
print(exemplo[-1])
print(exemplo[-2])
print(exemplo[-3])
print(exemplo[-4])
print(exemplo[-5])

#strings são imutáveis. Não se pode alterar os caracteres de uma string, apenas criar uma nova string

                                        #Concatenação
#Combinação de duas ou mais strings através do operador de adição

print("Angra" + " é" + " uma" + " banda")


                                        #Manipulação de strings
#É possível multiplicar string utilizando operador *

print("Angra"*3)

#É possível deixar em maiúsculas e minúsculas utilizando o método .upper() ou .lower()

print("Banda".upper())
print("BANDA".lower())

#Também é possível deixar apenas a primeira letra maiúscula utilizando o método .capitalize()

print("banda".capitalize())

                                        #Método Format

#É possível criar uma nova string utilizando o método format. Esse método procura novas ocorrências de chaves
# ({}) na string e substitui pelos parâmetros passados.

print("Iron {}".format("Maiden"))

#com variáveis

banda = "Maiden"
print("Iron {}".format(banda))

#as chaves podem ser usadas várias vezes

print("{} é uma {} de {}".format("Angra", "banda", "Power Metal"))

#com variáveis

a = "Angra"
b = "banda"
c = "Power Metal"

print("{} é uma {} de {}".format(a, b, c))

#exemplo de uso do format com input de usuário:

var_1 = input("Digite seu nome: ")
var_2 = int(input("Digite sua matrícula: "))
var_3 = input("Digite sua ocupação: ")

print("""Seja bem vindo, {}
Matrícula: {}
Cargo: {}""".format(var_1, var_2, var_3))


                                        #Método Split

#método usado para dividir uma string em duas ou mais strings. O resultado é uma lista com itens antes e depois do que tem no parâmetro
print("Olá! Sim, é isso mesmo. Toda a loja em promoção".split("."))

                                        #Método join

#Permite adicionar novos caracteres entre cada caractere de uma string

var_01 = "Olá"
resultado = "-".join(var_01)
print(resultado)

#é possível transformar ums lista de strings em uma única string chamando o método join em um string vazia

lista = ["O", "rato", "roeu", "a", "roupa", "do", "rei", "de", "Roma"]
use_join = " ".join(lista)
print(use_join)

#para remoção de espaços em branco iniciais e finais utiliza-se o método .strip()

palavra = " espaços "
palavra = palavra.strip()
print(palavra)

                                        #Método Replace
#substitui cada ocorência de uma string por outra string. O primeiro parâmetro é a string a ser substituida
# o segundo é a string que substituirá

exemplo_01 = "Palavra com a"
exemplo_01 = exemplo_01.replace("a", "@")                                   
print(exemplo_01)

                                        #Busca de um índice - método index
#Passe o caractere como parâmetro e o método index retornará o índice da primeira ocorrência desse caractere na string

print("bola".index("a"))

#caso não haja o caractere, será lançado uma exceção.
#exemplo para tratar a exceção:
try:
    print("bola".index("x"))
except ValueError:
    print("Caractere inexistente")

                                        #Palavra-chave in
#verifica se uma string existe em outra string e retorna True ou False

print("chuva" in "chuva de meteoros")                                         
print("coringa" in "Batman vs Superman")

#usando not para verificar se NÃO existe

print("chuva" not in "chuva de meteoros")                                         
print("coringa" not in "Batman vs Superman")

                                        #Escape de strings
#Escapar uma string é inserir um símbolo na frente de um caractere que tem algum significado pro Python. O Python usa
# barra invertida \ para o escape
#exemplo de como dá erro:
#print("Então ele disse: "Foi mesmo?" ")                                        
#exemplo correto:
print("Então ele disse: \"Foi mesmo?\" ")
#mais fácil: colocar aspas duplas dentro de aspas simples, ou vice-versa
print("Então ele disse: 'Foi mesmo?'")
print('Então ele disse: "Foi mesmo?"')

                                        #Nova linha
#\n dentro de uma string representa uma nova linha
print("linha1\nlinha2\nlinha3")      

                                        #Fatiamento
#é a maneira de retornar um novo iterável a partir de um subconjunto dos itens 
# de outro iterável
# O índice inicial é onde começa e o índice final é onde termina o fatiamento
#exemplo com uma lista:

bandas = ["Helloween",
    "Oficina G3",
    "Angra",
    "Megadeth"]
print(bandas[0:2])
#exemplo com string:

texto = "texto de teste"
print(texto[0:4])


