from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opção = int(input('>>>>> Qual é a sua Opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opção == 2:
        multiplicar = n1 * n2
        print(f'O resultado de {n1} x {n2} é {multiplicar}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção > 5:
        print('\033[31mOpção INVÁLIDA! tente novamente!\033[m')
    elif opção == 5:
        print('Finalizando...')
        sleep(3)
    print('=-='*10)
print('Fim do programa! volte Sempre!')






