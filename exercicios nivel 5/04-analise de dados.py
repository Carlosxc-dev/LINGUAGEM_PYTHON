num = (int(input('digite um numero: ')), int(input('digite um numero: ')), int(input('digite um numero: ')), int(input('digite um numero: ')), int(input('digite um numero: ')), )

print(f'o valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o valor 3 apreceu na {num.index(3)+1}ª posicao')
else:
    print('o valor 3 nao foi digitado')
print('os valores pares digitados foram: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')




