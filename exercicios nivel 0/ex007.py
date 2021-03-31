n1 = int(input("digita o n1:"))
n2 = int(input('digita o n2:'))
sm = n1 + n2
sb = n1 - n2
dv = n1 / n2
mt = n1 * n2
ep = n1 ** n2
rest = n1 % n2
dvi = n1 // n2

#print('a soma e:', sm, 'a subtração e:', sb)
#print('a muteplicação e:', mt, 'a divisao e:', dv)
#print('a expo e:', ep, 'o resto e:', rest, 'dvi e:', dvi)

print('a soma e {}\na divisao e {}\na subtração e {}\na mt {}\na ep {}'.format(
    sm, dv, sb, mt, ep))  # melhor jeito de fazer print
