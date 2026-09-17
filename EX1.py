import os
import re #Módulo para expressões regulares (avançadas)
os.system('cls')

nome = input("Digite seu nome completo: ")

print("Tamanho do nome:",len(nome))
print("Nome em maiúsculo: ", nome.upper())
print("Nome em minúsculo: ", nome.lower())
print("Nome invertido: ", nome[::-1])