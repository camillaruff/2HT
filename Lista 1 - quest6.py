#Lista 1 - quest6


#SOLICITACAO INFO
codigo = int(input("Digite o código do operário: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))

#CALCULO SALARIO
salario = horas_trabalhadas * 10.00

#VERIFICACAO DE HORAS E CALCULO DE PAGAGAMENTO EXTRA
if horas_trabalhadas > 50:
    horas_excedentes = horas_trabalhadas - 50
    pagamento_excedente = horas_excedentes * 20.00
else:
    horas_excedentes = 0
    pagamento_excedente = 0

#EXIBICAO
print("Salário total:", salario)
print("Salário excedente:", pagamento_excedente)