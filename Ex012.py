preço = float(input('Qual é o preço do produto? R$'))
des = preço - (preço * 5 / 100)
print(f'O produto que custava R${preço}')
print(f'Na promoção com desconto de 5% vai custar R${des:.2f}')
