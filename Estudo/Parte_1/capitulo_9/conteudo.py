#O python pode ser usado para trabalhar com arquivos, como ler e gravar dados
# Ler - acessar os dados desse arquivo
# Gravar - adicionar ou alterar os dados no arquivo
#primeiro deve-se abrir o caminho usando a função open. A função recebe dois parâmetros
# uma string representando o caminho (path), e outra representando o modo no qual será aberto

#modos para abrir arquivos:
# "r" abre somente para leitura
# "w" abre somente para gravação. Se existir, será sobrescrito, se não, será criado para gravação
# "w+" abre para leitura e gravação. Se existir, será sobrescrito, se não, será criado para leitura e gravação

#a função open retorna o objeto de arquivo. O método write faz gravação no arquivo e o método close fecha o arquivo.
#se abrir com o método open, deve-se fechar com close.
#exemplo:
ola = open("Estudo\Parte_1\capitulo_9\ola.txt", "w")
ola.write("Ola, Mundo!")
ola.close()

#lendo arquivo
with open("Estudo/Parte_1/capitulo_9/ola.txt", "r") as f:
    print(f.read())

#salvando em uma lista:

lista = list()
with open("Estudo/Parte_1/capitulo_9/ola.txt", "r") as f:
    lista.append(f.read())
print(lista)

# #Arquivos CSV
import csv

with open("Estudo/Parte_1/capitulo_9/teste.csv", "w", newline='') as f:
    w = csv.writer(f,
                   delimiter=",")
    w.writerow(["um",
                "dois",
                "tres"])
    w.writerow(["quatro",
                "cinco",
                "seis"])
    
#lendo arquivo csv:

with open("Estudo/Parte_1/capitulo_9/teste.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
