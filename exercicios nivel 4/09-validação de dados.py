sexo = str(input('digite seu sexo: ')).strip().upper()[0]
while sexo not in 'mMfF':
    sexo = str(input('dados invalidos, tente novamente: [m/f]'))
print('sexo {} validado com sucesso !'.format(sexo))

