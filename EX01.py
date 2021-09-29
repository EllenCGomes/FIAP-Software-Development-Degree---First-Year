bpm = int(input("Digite o seu numero de batimentos por minuto: "))
idade = int(input("Digite sua idade: "))
batimentos = "normal"

if idade > 65:
    if bpm < 50:
        batimentos = "abaixo"
    elif bpm > 60:
        batimentos = "acima"
    else:
        batimentos = "dentro"
    print("Seus batimentos se encontram {} da faixa adequada".format(batimentos))

elif idade >= 18:
    if bpm < 70:
        batimentos = "abaixo"
    elif bpm > 80:
        batimentos = "acima"
    else:
        batimentos = "dentro"
    print("Seus batimentos se encontram {} da faixa adequada".format(batimentos))

elif idade >= 8:
    if bpm < 80:
        batimentos = "abaixo"
    elif bpm > 100:
        batimentos = "acima"
    else:
        batimentos = "dentro"
    print("Seus batimentos se encontram {} da faixa adequada".format(batimentos))

elif idade <= 2:
    if bpm < 120:
        batimentos = "abaixo"
    elif bpm > 140:
        batimentos = "acima"
    else:
        batimentos = "dentro"
    print("Seus batimentos se encontram {} da faixa adequada".format(batimentos))
