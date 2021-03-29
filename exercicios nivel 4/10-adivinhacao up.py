from random import randint
comp = randint(0, 10)

print('-=-' * 20)
print('pensei em um numero de 0 a 10: ')
print("-=-" * 20)

acertos = False
palpite = 0

while not acertos:
    jogador = int(input('adivinhe qual e: '))
    palpite += 1
    if jogador == comp:
        acertos = True
    else:
        if jogador < comp:
            print('mais... tente dinovo')
        elif jogador > comp:
            print('menos...tente dinovo')
print('acertou com {} tentativas. PARABENS !!'.format(palpite))
