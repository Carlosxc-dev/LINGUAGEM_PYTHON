# medidas

n = float(input('escreva n: '))

print(n, 'metros vale:')
print((n/1000), 'km')
print((n/100), 'hm')
print((n/10), 'dam')
print((n*10), 'dc')
print((n*100), 'cm')
print('{:.0f} mm'.format(n*1000))
