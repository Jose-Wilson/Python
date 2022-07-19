soma = 0
conte = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        soma += cont
        conte += 1
print(f'A soma de todos {conte} os valores solicitados é {soma}')
