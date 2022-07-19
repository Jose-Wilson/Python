print('Gerador de PA')
print('-='*10)
t = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
term = t
cont = 1
while cont <= 10:
    print(f'{term} ->', end=' ')
    term += r
    cont += 1
print('FIM')
