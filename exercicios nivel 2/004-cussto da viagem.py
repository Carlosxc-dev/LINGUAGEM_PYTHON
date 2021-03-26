distancia = float(input('digite a distancia da viagem:  '))
print('voce esta prestes a começar uma viagem de {:.2f} KM'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('valor a ser pago e R$ {:.2f}'.format(preco))