vel = float(input('Qual é a velocidade atual do Carro: '))
if vel > 80:
    print('Multado! Você excedeu o limite permitido que é de 80Km/p')
    multa = (vel - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')
