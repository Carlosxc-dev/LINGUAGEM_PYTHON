# co = float(input('digite o cateto oposto:'))
# ca = float(input('digite o cateto adjacente'))
# hp = (co**2 + ca ** 2) ** (1/2)

import math
co = float(input('digite o cateto oposto:'))
ca = float(input('digite o cateto adjacente'))
hi = math.hypot(co, ca)

print('hipotenusa mede: {:.2f}'.format(hi))
