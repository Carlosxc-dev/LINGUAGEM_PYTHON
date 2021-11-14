from random import randint
from time import sleep
item = ('pedra', 'papel', 'tesoura')
comp = randint(0, 2)

print('-=' * 15)
print('------JOKENPO-------')
print('-=' * 15)

print('''suas opcoes sao:
[ 0 ] pedra 
[ 1 ] papel
[ 2 ] tesoura ''')

jogador = int(input('qual sua jogada: '))
print('jo')     # novos aprendizagem de tempo
sleep(1)
print('ken')
sleep(1)
print('po')
sleep(1)

print('-=' * 15)
print('o computador jogou {}'.format(item[comp]))
print('jogador jogou {}'.format(item[jogador]))
print('-=' * 15)

if comp == 0:  # comp jogo pedra
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador venceu')
    elif jogador == 2:
        print('computador venceu')
    else:
        print('jogada invalida')
elif comp == 1:  #comp jogo papel
    if jogador == 1:
        print('empate')
    elif jogador == 0:
        print('computador venceu')
    elif jogador == 2:
        print('jogador venceu')
    else:
        print('jogada invalida')
elif comp == 2:  #comp jogo tesoura
    if jogador == 2:
        print('impate')
    elif jogador == 0:
        print('computdor venceu')
    elif jogador == 1:
        print('jogador venceu')
    else:
        print('jaogada invalida')

