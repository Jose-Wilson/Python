valores = []
res = ' '
while True:
    valores.append(int(input('Digite um valor: ')))
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if res in 'N':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
