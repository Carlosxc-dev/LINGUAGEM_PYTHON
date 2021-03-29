print('-=' * 40)
print(' ' * 25, 'gerador de PA')
print('-=' * 40)

pri = int(input('fale numero: '))
razao = int(input('fale a razao: '))
termo = pri
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('quantos termos a mais mostrar? '))
print('fim, {} termos mostrados'.format(total))


