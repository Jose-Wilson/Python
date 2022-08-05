palavras = ('aprender', 'programar', 'linguagem', 'pythom',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\033[31m{letra}\033[m', end=' ')
