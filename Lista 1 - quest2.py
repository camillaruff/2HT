#Lista 1 - quest2


#PRECOS E CORES
tabela_precos = { #dicionário
    "Verde": "R$ 10,00",
    "Azul": "R$ 20,00",
    "Amarelo": "R$ 30,00",
    "Vermelho": "R$ 40,00"
}

#SOLICITACAO
cor = input("Digite a cor do jogo: ")

#CORRESPONDER
preco = tabela_precos.get(cor, "Cor inválida")

#EXIBICAO DO PRECO
print("Preço:", preco)