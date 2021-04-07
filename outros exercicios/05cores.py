from time import sleep

c = ('\033[m',           # 1 sem cores
     '\033[0;30;41m',    # 2 vermelho
     '\033[0;30;42m',    # 3 verde
     '\033[0;30;43m',    # 4 amarelo
     '\033[0;30;44m',    # 5 azul
     '\033[0;30;45m',    # 6 roxo
     '\033[7;30m'        # 7 branco 
    )


def ajuda(com):
    titulo(f'acessando manual de comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='') 
    sleep(1)


# programa principal
comando = ''
while True:
    titulo('sistema de ajuda pyhelp', 2)
    comando = str(input('biblioteca ou funcao > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO', 1)

