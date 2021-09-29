# Recebe tipo de assinatura e faturamento anual do cliente e considera bonus inicial de zero
tipo_assinatura = input("Digite o tipo de assinatura (Basic, Silver, Gold ou Platinum): ")
faturamento_anual = float(input("Digite seu faturamento anual: "))
bonus = 0

# Verifica o tipo de assinatura
if tipo_assinatura.capitalize() == "Basic":
    # Calcula bonus de 30% para plano basic
    bonus = faturamento_anual * 0.3
    print("O valor do bonus a ser pago é de R$", bonus)
elif tipo_assinatura.capitalize() == "Silver":
    # Calcula bonus de 20% para plano silver
    bonus = faturamento_anual * 0.2
    print("O valor do bonus a ser pago é de R$", bonus)
elif tipo_assinatura.capitalize() == "Gold":
    # Calcula bonus de 10% para plano gold
    bonus = faturamento_anual * 0.1
    print("O valor do bonus a ser pago é de R$", bonus)
elif tipo_assinatura.capitalize() == "Platinum":
    # Calcula bonus de 5% para plano platinum
    bonus = faturamento_anual * 0.05
    print("O valor do bonus a ser pago é de R$", bonus)
else:
    # Envia mensagem de erro caso o cliente digite errado
    print("Erro. Por favor escolha entre as assinaturas Basic, Silver, Gold ou Platinum.")
