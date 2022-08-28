from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + (dados['contratação'] + 35) - datetime.now().year
print('-='*20)
for i, v in dados.items():
    print(f'- {i} tem o valor {v}')




