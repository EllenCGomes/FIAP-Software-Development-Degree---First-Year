soma_impares = 0
soma_pares = 0

# recebe e soma notas impares
for i in range(1, 50, 2):
    print("Voce esta digitando as notas dos alunos impares")
    nota_impares = float(input("Por favor, insira a nota do aluno {}: ".format(i)))
    soma_impares = soma_impares + nota_impares
    
# recebe e soma notas pares
for i in range(2, 51, 2):
    print("Voce esta digitando as notas dos alunos pares")
    nota_pares = float(input("Por favor, insira a nota do aluno {}: ".format(i)))
    soma_pares = soma_pares + nota_pares

# calcula media das notas impares e pares
media_impares = soma_impares/25
media_pares = soma_pares/25

# verifica qual media 'e maior
if media_impares > media_pares:
    print("A media das notas impares foi {:.2f} e das notas pares {:.2f}, sendo que as impares obtiveram maior nota."
          .format(media_impares, media_pares))

elif media_impares < media_pares:
    print("A media das notas impares foi {:.2f} e das notas pares {:.2f}, sendo que as pares obtiveram maior nota."
          .format(media_impares, media_pares))
else:
    print("A media das notas impares e pares foram de {:.2f}.".format(media_impares))
