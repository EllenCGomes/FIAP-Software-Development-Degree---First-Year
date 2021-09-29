# Recebe dados votacao
segunda_feira = int(input("Digite a quantidade de votos para a segunda-feira: "))
terca_feira = int(input("Digite a quantidade de votos para a terca-feira: "))
quarta_feira = int(input("Digite a quantidade de votos para a quarta-feira: "))
quinta_feira = int(input("Digite a quantidade de votos para a quinta-feira: "))
sexta_feira = int(input("Digite a quantidade de votos para a sexta-feira: "))

# Checa se a segunda feira ganhou os votos
if segunda_feira > terca_feira and segunda_feira > quarta_feira and segunda_feira > quinta_feira and segunda_feira > \
        sexta_feira:
    print("O dia escolhido foi segunda-feira")
# Checa se a terca feira ganhou os votos
elif terca_feira > segunda_feira and terca_feira > quarta_feira and terca_feira > quinta_feira and terca_feira > \
        sexta_feira:
    print("O dia escolhido foi terca-feira")
# Checa se a quarta feira ganhou os votos
elif quarta_feira > segunda_feira and quarta_feira > terca_feira and quarta_feira > quinta_feira and quarta_feira > \
        sexta_feira:
    print("O dia escolhido foi quarta-feira")
# Checa se a quinta feira ganhou os votos
elif quinta_feira > segunda_feira and quinta_feira > terca_feira and quinta_feira > quarta_feira and quinta_feira > \
        sexta_feira:
    print("O dia escolhido foi quinta-feira")
# Checa se a sexta feira ganhou os votos
elif sexta_feira > segunda_feira and sexta_feira > terca_feira and sexta_feira > quarta_feira and sexta_feira > \
        quinta_feira:
    print("O dia escolhido foi sexta-feira")
# Mensagem caso de empate
else:
    print("A votacao deu empate. Por favor, tente novamente.")

