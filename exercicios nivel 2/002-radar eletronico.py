vel = float(input('qual e a velocidade atual do carro:  '))
if vel > 80:
    multa = (vel - 80) * 7
    print('voce foi multado em R$ {}'.format(multa))
print('bao viagem, dirija com segurança !!')
