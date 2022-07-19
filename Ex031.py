viag = float(input('Qual é a distância da viagem? '))
print(f'Você está prestes a começar uma viagem de {viag:.1f}Km.')
if viag <= 200:
    preço = viag * 0.50
    print(f'E o preço da sua passagem será de R${preço:.2f}')
else:
    preço = viag * 0.45
    print(f'E o preço da sua passagem será de R${preço:.2f}')

