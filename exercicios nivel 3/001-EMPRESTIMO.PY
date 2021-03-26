print('\033[0;37;46m->->\033[m'*10)
print('           {}EMPRESTIMOS{}'.format('\033[0;37;46m', '\033[m'))
print('\033[0;37;46m->->\033[m'*10)

casa = float(input('qual valor da casa ?  '))
salario = float(input('qual salario ? '))
anos = int(input('quantos anos de financiamento?  '))
prestacao = casa / (anos * 12)
minimo = salario * (30 / 100)

print('para pagar uma casa de {:.2f} em {} anos'.format(casa, anos))
print('a prestaacao sera de R$ {:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('o emprestimo pode ser concedido!!')
else:
    print('    {}emprestimo negado{}   '.format('\033[0;30;41m', '\033[m'))
