numero = list()
while True:
    n = int(input(f'digite um valor:  '))
    if n not in numero:
        numero.append(n)
        print(f'valor adicionado com sucesso..')
    else:
        print(f'valor duplicado nao vou adicionar..')
    r = str(input('quer continuar [S/N] '))
    if r in 'nN':
        break
print('-='*30)
numero.sort()
print(f'voce digitpu os valores {numero}')
    