def ficha(jog='Desconhecido', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Números de Gols: '))
print('-='*25)

if n.strip() == '':
    ficha(gol=0)
else:
    ficha(n, g)

if g.isnumeric():
    g = int(g)
else:
    g = 0



