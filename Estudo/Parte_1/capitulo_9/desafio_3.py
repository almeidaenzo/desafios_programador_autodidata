# Pegue os itens desta lista de listas, [["Top Gun", "Risky Business",
#  "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]] , e grave-os em um arquivo
#  CSV. Os dados de cada lista devem ser uma linha no arquivo, com cada item da lista separado por uma vírgula.
import csv

filmes =  [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("filmes.csv", "w") as f:
    lista = csv.writer(f, delimiter=',')
    for listas in filmes:
        lista.writerow(listas)
