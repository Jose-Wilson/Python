lista = []
pares = []
impares = []
while True:
    núm = int(input('Digite um número: '))
    lista.append(núm)
    if núm % 2 == 0:
        pares.append(núm)
    else:
        impares.append(núm)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de Ímpares é {impares}')
