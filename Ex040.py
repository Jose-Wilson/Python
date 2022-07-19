n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f} a média do aluno é {média:.1f}')
if média >= 7:
    print('O aluno está APROVADO!')
elif 5 <= média < 7:
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('O aluno está REPROVADO.')


