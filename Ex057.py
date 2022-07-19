sexo = str(input('Informe seu Sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso.')



