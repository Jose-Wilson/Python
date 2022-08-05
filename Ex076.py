print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
lista = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'transferidor', 4.20,
         'Compasso', 9.80,
         'Mochila', 120.30,
         'Canetas', 22.30,
         'Livros', 34.90)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('-'*40)
