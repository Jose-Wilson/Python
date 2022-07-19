from datetime import date
ano = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = ano - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {ano}.')
if idade < 18:
    alist = 18 - idade
    print(f'Ainda faltam {alist} anos para o alistamento')
    print(f'Seu alistamento sera em {ano + alist}.')
elif idade > 18:
    alist = idade - 18
    print(f'Você já deveria ter se alistado há {alist} anos.')
    print(f'Seu alistamento foi em {ano - alist}.')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')


