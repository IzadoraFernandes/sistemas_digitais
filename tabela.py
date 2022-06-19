import numpy as np

dicionario = {
    "caso1":"(A'.B'.C')", "caso2": "(A'.B'.C)","caso3":"(A'.B.C')", "caso4": "(A'.B.C)", 
    "caso5":"(A.B'.C')","caso6": "(A.B'.C)", "caso7":"(A.B.C')", "caso8": "(A.B.C)"
}

dicionario = dict(dicionario)

matriz_a =  ["A", 0, 0, 0, 0, 1, 1, 1, 1]
matriz_b =  ["B", 0, 0,1, 1, 0, 0, 1, 1]
matriz_c =  ["C", 0, 1, 0, 1, 0, 1, 0, 1]

linha1 = input("digite o resutado para a 1° linha ")
linha2 = input("digite o resutado para a 2° linha ")
linha3 = input("digite o resutado para a 3° linha ")
linha4 = input("digite o resutado para a 4° linha ")
linha5 = input("digite o resutado para a 5° linha ")
linha6 = input("digite o resutado para a 6° linha ")
linha7 = input("digite o resutado para a 7° linha ")
linha8 = input("digite o resutado para a 8° linha ")

matriz_x =  ["S", linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8 ]
matrix = [matriz_a, matriz_b, matriz_c, matriz_x]
resultado= []


if '1' in linha1:
    
    resultado.append(dicionario["caso1"])

if '1' in linha2:
    resultado.append(' + ')
    resultado.append(dicionario["caso2"])

if '1' in linha3:
    resultado.append(' + ')
    resultado.append(dicionario["caso3"])

if '1' in linha4:
    resultado.append(' + ')
    resultado.append(dicionario["caso4"])

if '1' in linha5:
    resultado.append(' + ')
    resultado.append(dicionario["caso5"])

if '1' in linha6:
    resultado.append(' + ')
    resultado.append(dicionario["caso6"])

if '1' in linha7:
    resultado.append(' + ')
    resultado.append(dicionario["caso7"])

if '1' in linha8:
    resultado.append(' + ')
    resultado.append(dicionario["caso8"])



print("\n", "$"*50, "\n", "TABELA VERDADE")

for i in  range(len(matrix)):
    print(matrix[i])
    i +=1

print("\n","$"*50)
print("Resultados das expressões booleanas são: ",resultado)

