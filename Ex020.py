from random import shuffle
p = str(input('Primeiro aluno: '))
s = str(input('Segundo aluno: '))
t = str(input('Terceiro aluno: '))
q = str(input('Quarto aluno: '))
list = [p, s, t, q]
shuffle(list)
print(f'{list}')
