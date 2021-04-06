from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not mod.arquivo.arquivoexiste(arq):
    mod.arquivo.criararquivo(arq)

while True:
    resposta = menu(['ver pessoas cadastradas', 'cadastrar pessoas', 'sair do app'])
    if resposta == 1:
        cabecalho('opcao 1')
    elif resposta == 2:
        cabecalho('opcao 2')
    elif resposta == 3:
        break
    else:
        print('\033[31mdigite uma opcao valida\033[m')
    sleep(2)
    