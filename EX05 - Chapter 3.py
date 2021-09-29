minutos_atuais = int(input("Digite os minutos que a maquina esta marcando: "))
fatorial = 1

for i in range(2, (minutos_atuais + 1)):
    fatorial = fatorial * i

print("A senha sera LIBERDADE{}".format(fatorial))
