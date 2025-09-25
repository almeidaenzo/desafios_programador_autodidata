#Escreva um programa que colete duas strings com um usuário, insira-as na string 
# "Yesterday I wrote a [resposta_um]. I sent it to [resposta_dois]!" e exiba uma nova string.

resposta_um = input("Write the first Word: ")
resposta_dois = input("Write the second word: ")

print("Yesterday I wrote a {}. I sent it to {}!".format(resposta_um, resposta_dois))