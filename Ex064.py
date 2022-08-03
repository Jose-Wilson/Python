núm = cont = soma = 0
núm = int(input('Digite um número [555 para parar]: '))
while núm != 555:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [555 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
