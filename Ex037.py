num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converte para BINÁRIO')
print('[ 2 ] converte para  OCTAL')
print('[ 3 ] converte para EXADECIMAL')
op = int(input('Sua opção: '))
if op == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif op == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
else:
    print(f'{num} convertido para EXADECIMAL é igual a {hex(num)[2:]}')
