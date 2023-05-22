#Lista 1 - quest8


#SOLICITAR INFO
numero = int(input("Digite um número inteiro: "))

#VERIFICACAO
primo = True
if numero > 1:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break
else:
    primo = False

#EXIBICAO
if primo:
    print(numero, "é primo.")
else:
    print(numero, "não é primo.")