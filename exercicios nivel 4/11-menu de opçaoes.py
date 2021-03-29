from time import sleep
n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] soma
    [2] multeplicar
    [3] maior
    [4] novos numeros
    [5] sair''')
    opcao = int(input('>>>>>>>qual e sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('a soma {} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        mut = n1 * n2
        print('a multiplicação {} * {} = {}'.format(n1, n2, mut))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('o maior e {}'.format(maior))
        else:
            maior = n2
            print('o maior e {}'.format(maior))
    elif opcao == 4:
        print('fale novante: ')
        n1 = int(input('primeiro valor: '))
        n2 = int(input('segundo valor: '))
    elif opcao == 5:
        print('finalizando.....')
    else:
        print('opcao invalida')
    print('-=-' * 20)
    sleep(2)
print('FIM DO PROGRAMA !!')
