def fatorial(n, show=False):
    """
    -> calcula fatorial de um numero:
    param n: numero para calcular
    param show: (opcional) mostra ou nao a conta
    return: o valor do fatorial de um numero n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f = f + c
    return f



# programa principal
print(fatorial(5, show=True))
help(fatorial)
