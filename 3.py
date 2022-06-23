dicionario = {
    "caso1":"(A'.B'.C')", "caso2": "(A'.B'.C)","caso3":"(A'.B.C')", "caso4": "(A'.B.C)", 
    "caso5":"(A.B'.C')","caso6": "(A.B'.C)", "caso7":"(A.B.C')", "caso8": "(A.B.C)"
}

dicionario = dict(dicionario)

i = 0
resultado = []
linhas = []
s = ['S']
tabela = [['A', '0', '0', '0', '0', '1', '1', '1', '1'], ['B','0', '0','1', '1','0', '0','1', '1'],['C',
'0','1','0','1','0','1','0','1'],[s] ]

print('preencha a tabela verdade com a saída para obter as expressões booleanas:')
for i in range(8):
    linha_i = input(f' linha {i} :')
    if linha_i != '1' and linha_i != '0':
        print('ERRO digite apenas 1 ou 0')
        linha_i = input(f' linha {i} :')

    linhas.append(linha_i)
    s.append(linha_i)
    i += 1


if linhas[0] == '1':

    resultado.append(dicionario["caso1"])

if linhas[1] =='1':
    resultado.append('+')
    resultado.append(dicionario["caso2"])

if linhas[2] =='1':
    resultado.append('+')
    resultado.append(dicionario["caso3"])

if linhas[3] =='1':
    resultado.append('+')
    resultado.append(dicionario["caso4"])

if linhas[4] =='1':
    resultado.append('+')
    resultado.append(dicionario["caso5"])

if linhas[5] =='1':
    resultado.append('+')
    resultado.append(dicionario["caso6"])

if linhas[6] =='1':
    resultado.append('+')
    resultado.append(dicionario["caso7"])

if linhas[7] =='1':
    resultado.append('+')
    resultado.append(dicionario["caso8"])

teste = ''.join(resultado)
print(*tabela,sep="\n")
print (teste)