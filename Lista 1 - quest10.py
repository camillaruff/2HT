#Lista 1 - quest10


#SOLICITAR INFO
distancia = float(input("Digite a distância percorrida (em quilômetros): "))
combustivel = float(input("Digite a quantidade de combustível gasta (em litros): "))

#CALCULO CONSUMO MEDIO
consumo_medio = distancia / combustivel
#CALCULO GASTO COMBUSTIVEL
gasto_combustivel = 4.50 * combustivel 

#EXIBICAO
print(f"Consumo médio: {consumo_medio:.2f} km/l")
print(f"Gasto com combustível: R$ {gasto_combustivel:.2f}")