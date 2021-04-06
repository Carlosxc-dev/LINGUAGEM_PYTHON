def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res) # uma forma


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res) # outra forma 


def moeda(preco=0, moeda='R$ ', formato=False):
    return F'{moeda}{preco:>.2f}'.replace('.',',')


def resumo(preco=0, taxaa=10, taxar=20):
    print('--' * 40)
    print('RESUMO DO VALOR'.center(50))
    print('--' * 40)
    print(f'preço analizado:        \t{moeda(preco)}')
    print(f'o dobro do preço:       \t{dobro(preco, True)}')
    print(f'a metade do preço:      \t{metade(preco, True)}')
    print(f'a aumentando 10% temos: \t{aumentar(preco, taxaa, True)}')
    print(f'a dimiuir de 20% temos: \t{diminuir(preco, taxar, True)}')
    print('--' * 40)
