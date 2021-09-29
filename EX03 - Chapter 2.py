funcionario1 = input("Digite o primeiro voto, escolhendo entre as opcoes PLAYSTATION, XBOX ou NINTENDO: ")
funcionario2 = input("Digite o segundo voto: ")
funcionario3 = input("Digite o terceiro voto: ")
funcionario4 = input("Digite o quarto voto: ")
funcionario5 = input("Digite o quinto voto: ")

playstation = 0
xbox = 0
nintendo = 0

if funcionario1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif funcionario1.upper() == "XBOX":
    xbox = xbox + 1
else:
    nintendo = nintendo + 1

if funcionario2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif funcionario2.upper() == "XBOX":
    xbox = xbox + 1
else:
    nintendo = nintendo + 1

if funcionario3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif funcionario3.upper() == "XBOX":
    xbox = xbox + 1
else:
    nintendo = nintendo + 1

if funcionario4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif funcionario4.upper() == "XBOX":
    xbox = xbox + 1
else:
    nintendo = nintendo + 1

if funcionario5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif funcionario5.upper() == "XBOX":
    xbox = xbox + 1
else:
    nintendo = nintendo + 1

if playstation >= 3:
    print("O console escolhido foi o PLAYSTATION com {} votos".format(playstation))
elif xbox >= 3:
    print("O console escolhido foi o XBOX com {} votos".format(xbox))
elif nintendo >= 3:
    print("O console escolhido foi o NINTENDO com {} votos".format(nintendo))
else:
    print("Deu empate. Por favor, realize uma nova votacao")

