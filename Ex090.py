aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'
print('-='*20)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')

