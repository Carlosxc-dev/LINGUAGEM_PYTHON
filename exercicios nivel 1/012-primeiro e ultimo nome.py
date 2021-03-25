n = str(input('fala nome: ')).strip()
nome = n.split()

print('muito prazer em te conehcer ')
print('seu primeiro nome e {}'.format(nome[0]))
print('e o ultimo e {}'.format(nome[len(nome)-1]))
