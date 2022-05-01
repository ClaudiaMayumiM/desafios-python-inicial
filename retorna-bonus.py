# Criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês.

assinatura = input('Por favor, informe seu nível de assinatura: ').upper()
fat_anual = float(input('Por favor, informe o valor (R$) do seu faturamento anual: '))

if assinatura == 'BASIC': 
    bonus = fat_anual * 0.3
    print(f'Você deve pagar um bônus de R${bonus} ao prestador do serviço de estúdio.')
elif assinatura == 'SILVER':
    bonus = fat_anual * 0.2
    print(f'Você deve pagar um bônus de R${bonus} ao prestador do serviço de estúdio.')
elif assinatura == 'GOLD':
    bonus = fat_anual * 0.1
    print(f'Você deve pagar um bônus de R${bonus} ao prestador do serviço de estúdio.')
elif assinatura == 'PLATINUM':
    bonus = fat_anual * 0.05
    print(f'Você deve pagar um bônus de R${bonus} ao prestador do serviço de estúdio.')
else:
    print('Não é um nível de assinatura válido!')