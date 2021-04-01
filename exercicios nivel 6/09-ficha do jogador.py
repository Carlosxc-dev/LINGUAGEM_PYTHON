def ficha(jog='<desconhecido>', gol=0):
    print(f'o {jog} consegiu fazer {gol} gol no campeonato')


# program principal
n = str(input('nome do jogador: '))
g = str(input('qquantos gol fez: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
