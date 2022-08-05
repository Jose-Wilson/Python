from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10),
     randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for n in num:
    print(f'\033[32m{n}\033[m', end='  ')
print(f'\nO maior valor sorteado foi \033[34m{max(num)}\033[m')
print(f'O menor valor sorteado foi \033[31m{min(num)}\033[m')
