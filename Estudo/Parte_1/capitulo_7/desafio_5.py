#Multiplique todos os números da lista [8, 19, 148, 4] por todos os números da lista [9, 1, 33, 83]
#e acrescente cada resultado a uma terceira lista


lista_1 = [8, 19, 148, 4]
lista_2 = [9, 1, 33, 83]
mult = []

for i in lista_1:
    for j in lista_2:
        mult.append(i * j)

print(mult)