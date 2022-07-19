sal = float(input('Qual é o salário do Funcionário? R$ '))
aumento = sal + (sal * 15 / 100)
print(f'Um funcionário que ganhava R${sal:.2f}')
print(f'Com 15% de aumento, passa a receber R${aumento:.2f}')
