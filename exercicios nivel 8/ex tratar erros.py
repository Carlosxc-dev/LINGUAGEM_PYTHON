def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mdigite um numero inteiro valido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31musuario nao quis digitar o numero\033[31m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mdigite um numero inteiro valido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31musuario nao quis digitar o numero\033[31m')
            return 0
        else:
            return n


n1 = leiaint('digite um numero inteiro: ')
n2 = leiafloat('digite um numero real: ')
print(f'o inteiro digitado e {n1} e o real e {n2}')
