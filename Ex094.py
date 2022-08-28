pessoa = {}
galera = []
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('-='*25)
        print('ERRO! Por Favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('-='*25)
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
    print('-='*25)
print('-='*25)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')

print('C) As mulheres cadastradas foram!')
for m in galera:
    if m['sexo'] in 'F':
        print(f'{m["nome"]} ', end='')
print('\n')

print('D) Lista das pessoas que estão acima da média!')
for p in galera:
    if p['idade'] >= média:
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print()
print('   <<<  ENCERRADO  >>>   ')
