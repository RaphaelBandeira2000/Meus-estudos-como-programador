import random
numero = [
    ('n1', 1),
    ('n2', 2),
    ('n3', 3),
    ('n4', 4),
    ('n5', 5)
]
while True: 
    tupla_aleatoria = random.choice(numero)
    numero_int = int(tupla_aleatoria[1])
    nmr = int(input('chute um numero entre 1 a 5: '))
    if nmr == numero_int: 
        print('Vc acertou!')
    else:
        print('Vc errou, tente novamente')
    print(f'O numero foi: {tupla_aleatoria[1]}')
    continuar_jogando = input('Continuar jogando? sim ou nao? ')
    if continuar_jogando.lower() != 'sim':
        print('Obrigado por jogar!')
        break
    else:
        print('recomeçando')