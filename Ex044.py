print('='*12, 'LOJAS GUANABARA', '='*12)
preço = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opção = int(input('Qual é a opção: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
    print(f'Sua compra de R${preço:.2f} à vista! ')
    print(f'Ela vai custar com 10% de desconta, vai custar R${total:.2f}')
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de {parcela:.2f} SEM JUROS')
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = preço + (preço * 20 / 100)
    parcela = total / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de {parcela:.2f} COM JUROS')
else:
    total = 0
    print(f'\033[31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[m')
    opção = int(input('Qual é a opção? '))
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final')
