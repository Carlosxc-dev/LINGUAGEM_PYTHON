listanum = []
mai = 0
men = 0
for c in range(0, 4):
    listanum.append(int(input(f'digite um valor para posição {c}: ')))
    if c == 0:
        mai == men == listanum[c]
    else:
        if listanum[c] > mai:
           mai = listanum[c]   
        if listanum[c] < men:
            men = listanum[c]
print('-='*30)
print(f'voce digitou os valores {listanum}')
print(f'o maior valor digitado foi {mai} nas posicoes ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'o menor valor digitado foi {men} nas posicoes ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()
