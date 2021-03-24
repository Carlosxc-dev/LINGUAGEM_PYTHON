#import random
#n1 = input('nome do aluno:')
#n2 = input('nome do aluno:')
#n3 = input('nome do aluno:')
#n4 = input('nome do aluno:')
#lista = [n1, n2, n3, n4]
#escolhido = random.choice(lista) # aleatorio
#print('o aluno escolhido foi {}'.format(escolhido))

import random
n1 = input('nome do aluno:')
n2 = input('nome do aluno:')
n3 = input('nome do aluno:')
n4 = input('nome do aluno:')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('a ordem escolhida é\n{}'.format(lista))
