num = cont = soma = 0
num = int(input('fale um numero [999 pra parar: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('fale um numero [999 pra parar: '))
print('voce digitou {} numeros e soma entre eles foi {}'.format(cont, soma))





