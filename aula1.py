selecoes = ['malásia,'
            'China',
            'gabão',
            'malta'
            ]

selecao = input('digite a seleção desejada: ')
find = False

for i in range(len(selecoes)):

    if selecao.upper() == selecoes[i].upper():
        find = True

if find:
    print('achei!')
else:
    print('não achei')