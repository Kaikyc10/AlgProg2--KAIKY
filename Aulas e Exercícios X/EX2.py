import os
import re #Módulo para expressões regulares (avançadas)
os.system('cls')

frase = input("Digite uma frase: ")
palavra = ""
ultima= ""



for i in range(0,len(frase),1):
    if frase[i].isalpha():
        palavra = palavra + frase[i]
    if not frase[i].isalpha():
        break

for j in range(len(frase) -1,-1,-1):
    if frase[j].isalpha():
        ultima = ultima + frase[j]
    if not frase[j].isalpha():
        break


palavras = frase.split()
print("Quantidade de palavras:",len(palavras))
print("Primeira palavra: ", palavra)
print("Última palavra: ",ultima[::-1])
