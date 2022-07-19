frase = str(input('Digite uma frase: ')).upper().strip().split()
junto = ''.join(frase)
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('A frase digitada é um Palíndromo!')
else:
    print('A frase digitada Não é um Palíndromo!')
