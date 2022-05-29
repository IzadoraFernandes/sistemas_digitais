
print (''' Escolha uma das bases para conversão:
[1] Conversão de BÍNARIO para DECIMAL
[2] Conversão de OCTAL para DECIMAL
[3] Converter de HEXADECIMAL para DECIMAL
''')
opcao = int(input("Digite um número de acordo com a conversão desejada:"))

if opcao == 1:
    binario=list(input("Digite um numero para converter de BINARIO para DECIMAL: "))
    total_binario =0
    char_binario=len(binario) #retornar o comprimento da lista


    for i in range(char_binario):
        last_elemento_binario=binario.pop() #retorna e elimina o ultimo elemento da lista
        if last_elemento_binario=="1":
            total_binario += pow(2,i)

    print (f' convertido para decimal é = {total_binario}')

elif opcao ==2:
    octal=list(input("Digite um numero de 0 a 8 para converter de OCTAL para DECIMAL: "))
    total_octal =0
    char_octal=len(octal) #retornar o comprimento da lista


    for i in range(char_octal):
        last_elemento_octal= octal.pop() #retorna e elimina o ultimo elemento da lista

        if last_elemento_octal=="1":
            total_octal += pow(8,i) * 1

        elif last_elemento_octal=="2":
            total_octal += pow(8,i) * 2

        elif last_elemento_octal=="3":
            total_octal += pow(8,i) * 3

        elif last_elemento_octal=="4":
            total_octal += pow(8,i) * 4

        elif last_elemento_octal=="5":
            total_octal += pow(8,i) * 5

        elif last_elemento_octal=="6":
            total_octal += pow(8,i) * 6

        elif last_elemento_octal=="7":
            total_octal += pow(8,i) * 7
    
        elif last_elemento_octal=="8":
            total_octal += pow(8,i) * 8

        elif last_elemento_octal=="0":
            total_octal += pow(8,i) * 0



    print (f' convertido para decimal é = {total_octal}')

elif opcao ==3:

    hexadecimal=list(input("Digite um numero para converter de HEXADECIMAL para DECIMAL: "))
    total_hexadecimal =0
    char_hexadecimal=len(hexadecimal) #retornar o comprimento da lista

    for i in range(char_hexadecimal):
        last_elemento_hexadecimal=hexadecimal.pop() #retorna e elimina o ultimo elemento da lista
        x=last_elemento_hexadecimal
        if x == '1':
            total_hexadecimal += (16**i) * 1

        elif x == '2':
            total_hexadecimal += (16**i) * 2

        elif x == '3':
            total_hexadecimal += (16**i) * 3

        elif x == '4':
            total_hexadecimal += (16**i) * 4

        elif x == '5':
            total_hexadecimal += (16**i) * 5

        elif x == '6':
            total_hexadecimal += (16**i) * 6

        elif x == '7':
            total_hexadecimal += (16**i) * 7

        elif x == '8':
            total_hexadecimal += (16**i) * 8

        elif x == '9':
            total_hexadecimal += (16**i) * 9

        elif x.lower() == "a": #função lower a sua função é converter letras maiusclas para minúsculas
            total_hexadecimal += (16**i) *10

        elif x.lower() == "b":
            total_hexadecimal += (16**i) *11

        elif x.lower() == "c":
            total_hexadecimal += (16**i) *12

        elif x.lower() == "d":
            total_hexadecimal += (16**i) *13

        elif x.lower() == "e":
            total_hexadecimal += (16**i) *14

        elif x.lower() == "f":
            total_hexadecimal += (16**i) *15

        elif x.lower() == "0":
            total_hexadecimal += (16**i) *0
        

    print (f' convertido para decimal é = {total_hexadecimal}')
