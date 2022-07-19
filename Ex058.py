from random import randint
computador = randint(1, 10)
print('Sou seu computador....')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
cont = 0
palpite = 0
while not palpite == computador:
    palpite = int(input('Qual é o seu palpite? '))
    cont += 1
    if palpite < computador:
        print('Mais... Tente mais uma vez!')
    if palpite > computador:
        print('Menos... Tente mais uma vez!')
print(f'Acertou com {cont} tentativas. Parabéns!')

