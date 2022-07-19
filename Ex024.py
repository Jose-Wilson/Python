nome = str(input('Em que cideda você nasceu? ')).strip().upper()
separa = nome.split()
tem = 'SANTO' in separa[0]
print(tem)
