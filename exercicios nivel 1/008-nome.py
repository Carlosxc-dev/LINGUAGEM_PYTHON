nome = str(input('fale seu nome todo: ')).strip()
print('analizando seu nome: {}'.format(nome))
print('seu nome maiusculo e: {}'.format(nome.upper()))
print('seu nome minusculo e: {}'.format(nome.lower()))
print('total de letras e: {}'.format(len(nome) - nome.count(" ")))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome e {} e tem {} letras'.format(separa[0], len(separa[0])))
