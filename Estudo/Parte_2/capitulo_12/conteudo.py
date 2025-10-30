                                    #Programação Orientada a Objetos                                        
                                        #Paradigmas de Programação
#um paradigma de programação é um estilo de pogramação
#Na POO, as classes definem um conjunto de objetos que podem interagir uns com os outros
#objeto - instância de uma classe 
# sintaxe para imprmir uma classe - class [nome]:
#                                       [blocos]
# primeiro parâmetro de um método sempre começa com self

class Laranja:
    def __init__(self, p, c):
        self.peso = p
        self.cor = c
    print("Objeto Criado!")


laranja = Laranja(45.6, "verde")
print(laranja)

#sintaxe para obter os valores da variável de instância

class Laranja:
    def __init__(self, p, c):
        self.peso = p
        self.cor = c
    print("Objeto Criado!")


laranja = Laranja(45.6, "verde")
laranja.peso = 134.89
laranja.cor = "vermelho"

print(laranja.peso)
print(laranja.cor)



