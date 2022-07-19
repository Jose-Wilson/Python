sal = float(input('Qual é o salário do funcionário? R$ '))
if sal <= 1250:
    acres = (sal * 15 / 100) + sal
    print(f'Quem ganhava R${sal:.2f} passa a ganhar R${acres:.2f} agora.')
else:
    acres = (sal * 10 / 100) + sal
    print(f'Quem ganhava R${sal:.2f} passa a ganhar R${acres:.2f} agora.')

