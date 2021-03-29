frase = str(input('escreva a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('temos um palindromo')
else:
    print('nao e palindromo')
