cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('digite um numero de 0 a 10: '))
    if 0 <= num <= 20:
        break
    print('tente novamente: ')
print(f'voce digitou o numero {cont[num]}')

    
    