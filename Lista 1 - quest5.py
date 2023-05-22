#Lista 1 - quest5


#SOLICITAR INFO
peso_peixes = float(input("Digite o peso de peixes (em quilos): "))

#VERIFICACAO DE EXECESSO
excesso = max(0, peso_peixes - 50)
#CALCULO DA MULTA
multa = excesso * 4.00

#EXIBICAO
print("Excesso:", excesso)
print("Multa:", multa)