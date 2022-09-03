def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\33[m')
        if ok:
            break
    return valor


n = leiaint('Digite um Número: ')
print(f'Você acabou digitar o número {n}')
