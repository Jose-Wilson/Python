from Ex107 import moeda

p = float(input('Digite o preço: '))
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f}')
print(f'O dobro de R${p:.2f} é R${moeda.dobro(p):.2f}')
print(f'Aumentando 10%, temos F${moeda.aumento(p, 10):.2f}')

