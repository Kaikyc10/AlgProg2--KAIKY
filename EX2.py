import os
import re #Módulo para expressões regulares (avançadas)
os.system('cls')

frase = input("Digite uma frase: ")
contador = 0
palavra = ""
ultima= ""

for i in range(0,len(frase),1):
    if frase[i].isalnum():
        contador = contador + 1

for j in range(0,len(frase),1):
    if frase[j].isalpha():
        palavra = palavra + frase[j]
    if not frase[j].isalpha():
        break

for k in range(len(frase) -1,-1,-1):
    if frase[k].isalpha():
        ultima = ultima + frase[k]
    if not frase[k].isalpha():
        break


palavras = frase.split()
print("Quantidade de palavras:",len(palavras))
print("Primeira palavra: ", palavra)
print("Última palavra: ",ultima[::-1])
