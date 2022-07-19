print('Digite um número para')
n = int(input('Calcular seu Fatorial: '))
print(f'Calculando {n}! =', end=' ')
c = n
f = 1
while c > 0:
    print(f'{c}', end=' ')
    print(f'x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f'{f}')
