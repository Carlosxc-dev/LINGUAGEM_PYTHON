def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO->digite um numero inteiro valido\033[m')
        if ok:
            break
    return valor


# programa principal 
n = leiaint('digite um numero:  ')
print(f'voce acabou de digitar o numero {n}')
