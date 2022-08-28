time = []
partidas = []
jogador = {}

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-='*25)
        if resp in 'SN':
            break
        print('\033[31mERRO! Escolha apenas S ou N.\033[m')
    if resp == 'N':
        break

print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<20} ', end='')
print()

for k, v in enumerate(time):
    print(f'{k:>2}  ', end='')
    for d in v.values():
        print(f'{str(d):<21} ', end='')
    print()
print('-='*25)

while True:
    busca = int(input('Mostra dados de qual jogador? (555 para parar) '))
    if busca == 555:
        break
    if busca >= len(time):
        print(f'\033[31mERRO! Não existe Jogador com código {busca}\033[m')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR: {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i} fez {g} gols')
    print('-='*25)
print(' \033[32m<<<< VOLTE SEMPRE >>>>  ')
