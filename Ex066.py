soma = cont = 0
while True:
    núm = int(input('Digite um valor: '))
    if núm == 999:
        break
    cont += 1
    soma += núm
print(f'A soma dos {cont} valores foi {soma}!')
