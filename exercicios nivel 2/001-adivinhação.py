from random import randint
comp = randint(0, 5)
print('-=-' * 20)
print('advinhe um numero que pensei de 0 a 5')
pessoa = int(input('escolha um numero que eu pensei: '))
print("-=-" * 20)
if pessoa == comp:
    print('\nparabens acertou !!!')
else:
    print("errrooouuu ahahahaha")
print('eu pensei em {}\n'.format(comp))
