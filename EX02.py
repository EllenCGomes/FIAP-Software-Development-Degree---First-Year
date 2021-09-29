valor_bruto = float(input("Digite o valor bruto do pacote de viagem: "))
categoria = int(input("Escolha da Categoria: Digite 1 para Economica, 2 para Executiva ou 3 para Primeira Classe: "))
quantidade_viajantes = int(input("Digite a quantidade de viajantes: "))
desconto = 0

if quantidade_viajantes >= 4:
    if categoria == 1:
        desconto = 5
    elif categoria == 2:
        desconto = 8
    elif categoria == 3:
        desconto = 20
    valor_liquido = valor_bruto - (valor_bruto * (desconto / 100))
    valor_medio = valor_liquido / quantidade_viajantes
    print("Dados: valor bruto = {}, desconto = {}%, valor liquido = {} e valor medio por viajante = {}".format(
        valor_bruto, desconto, valor_liquido, valor_medio))

elif quantidade_viajantes == 3:
    if categoria == 1:
        desconto = 4
    elif categoria == 2:
        desconto = 7
    elif categoria == 3:
        desconto = 15
    valor_liquido = valor_bruto - (valor_bruto * (desconto / 100))
    valor_medio = valor_liquido / quantidade_viajantes
    print("Dados: valor bruto = {}, desconto = {}%, valor liquido = {} e valor medio por viajante = {}".format(
        valor_bruto, desconto, valor_liquido, valor_medio))

elif quantidade_viajantes == 2:
    if categoria == 1:
        desconto = 3
    elif categoria == 2:
        desconto = 7
    elif categoria == 3:
        desconto = 5
    valor_liquido = valor_bruto - (valor_bruto * (desconto / 100))
    valor_medio = valor_liquido / quantidade_viajantes
    print("Dados: valor bruto = {}, desconto = {}%, valor liquido = {} e valor medio por viajante = {}".format(
        valor_bruto, desconto, valor_liquido, valor_medio))

else:
    valor_liquido = valor_bruto
    valor_medio = valor_liquido / quantidade_viajantes
    print("Dados: valor bruto = {}, nao havera desconto, valor liquido = {} e valor medio por viajante = {}".format(
        valor_bruto, valor_liquido, valor_medio))

