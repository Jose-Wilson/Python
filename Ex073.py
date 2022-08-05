time = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
        'Flamengo', 'Vasco', 'Chapecoense', 'Atlético,', 'Botafogo',
        'Atlético-PR','Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
        'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('-=' * 20)
print(f'Lita de times do Brasileirão: {time}')
print('-=' * 20)
print(f'Os 5 Primeiros são: {time[:5]}')
print('-=' * 20)
print(f'Os 4 Últimos são: {time[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(time)}')
print('-=' * 20)
print(f'O Chapecoense está na {time.index("Chapecoense")+1}ª posição')
