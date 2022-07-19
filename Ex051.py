print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)
t1 = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
décimo = t1 + (10 - 1) * raz
for c in range(t1, décimo + raz, raz):
    print(c, end=' -> ')
print('ACABOU')
