num = int(input('fale um numero inteiro:  '))
print('''escolha umas das bases para conversao:
[ 1 ] binario  
[ 2 ] octal
[ 3 ] hexadecimal''')
opcao = int(input('sua opçaõ:  '))
if opcao == 1:
    print('{} convertido par binario fica {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal fica {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal fica {}'.format(num, hex(num)[2:]))
else:
    print('opcao invalida: tente novamente')
