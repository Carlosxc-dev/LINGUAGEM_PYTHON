def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('houve um erro na criacao do arquivo')
    else:
        print(f'arquivo {nome} criado com sucesso ')
    

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('erro ao ler arquivo')
    else:
        ('PESSOAS CADASTRADAS')
        print(a.read())