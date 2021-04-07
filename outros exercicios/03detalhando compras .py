total = totalmil = menor = cont = 0.0
barato = ''
while True:
    produto = str(input('nome do produto: '))
    preco = float(input('valor do produto: '))
    cont += 1
    total += preco
    if preco >= 1000:
        totalmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('continua ? s/n: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'fim do programa:-^40')
print(f'o total da compra foi {total}')
print(f'temos {totalmil} custando mais de mil reais')
print(f'o produto mais barato foi {barato} custando {menor}')

