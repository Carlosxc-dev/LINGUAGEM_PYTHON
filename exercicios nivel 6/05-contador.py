from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*30)
    print(f'contaagem de {i} ate {f} de {p} em {p} ')
    sleep(1.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='', flush=True)
            sleep(0.5)
            cont += p
        print('fim.....')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}  ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('fim.....')

# programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*30)
print('agora e sua vez de personalizar a contagem')
ini = int(input('inicio:  '))
fim = int(input('fim:     '))
pas = int(input('passo:   '))
contador(ini, fim, pas)


