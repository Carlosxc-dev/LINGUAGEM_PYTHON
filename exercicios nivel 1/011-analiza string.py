frase = str(input('fale seu nome: ')).lower().strip()

print("a letra A aparece {} vezes".format(frase.count('a')))
print("a primeira letra A aparece na posicao {}".format(frase.find('a')+1))
print("a ultima letra A apraceu na posição{}".format(frase.rfind('a')+1))
