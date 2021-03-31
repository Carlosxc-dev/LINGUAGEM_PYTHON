def area(larg, comp):
    a = larg * comp
    print(f'a are a de um terreno {larg} x {comp} e de {a} m2')


# programa principal
print('contrtole de valores ')
print('-=' * 30)
c = float(input('comprimento: '))
l = float(input('largura: '))
area(l, c)
