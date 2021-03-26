peso = float(input('escreva seu peso:  '))
altura = float(input('escreva sua altura:  '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('voce esta ABAIXO do peso normal ')
elif 18.5 <= imc < 25:
    print('parabenss peso NORMAL ') 
elif 25 <= imc < 30:
    print('voce esta ACIMA do peso')
elif 30 <= imc < 40:
    print('voce esta OBESO sua baleia')
elif imc > 40:
    print('precisa de tratamEnto, OBESIDADE MORBIDA')
    