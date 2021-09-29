# Recebe peso e altura
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

# Verifica se as variaveis sao diferentes de zero para poder calcular o IMC
if altura != 0 and peso != 0:

    # Calcula o IMC
    imc = peso/(altura**2)

    # Analisa a classificacao em que o IMC do individuo esta, de acordo com tabela pre enviada para uso
    if imc >= 40:
        print("Obesidade Grau III")
    elif imc >= 35:
        print("Obesidade Grau II")
    elif imc >= 30:
        print("Obesidade Grau I")
    elif imc >= 25:
        print("Sobrepeso")
    elif imc >= 18.5:
        print("Peso ideal")
    elif imc >= 17:
        print("Baixo peso Grau I")
    elif imc >= 16:
        print("Baixo peso Grau II")
    else:
        print("Baixo peso Grau III")
else:
    # Mostra mensagem de erro caso alguma variavel seja igual a zero
    if altura == 0 or peso == 0:
        print("Erro. Digite um numero maior que 0.")
