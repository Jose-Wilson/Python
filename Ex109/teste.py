from Ex109 import moeda

p = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumento de 10%, temos {moeda.aumento(p, 10, True)}')

