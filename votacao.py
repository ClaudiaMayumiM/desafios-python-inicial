# Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives. Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.

segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

for dia in range(2, 7, 1):
    votos = int(input(f'Por favor, informe a quantidade de votos da {dia}ª-feira: '))

    if dia == 2:
        segunda += votos 
    elif dia == 3:
        terca += votos 
    elif dia == 4:
        quarta += votos 
    elif dia == 5:
        quinta += votos 
    else:
        sexta += votos 

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print(f'O dia mais votado para a live foi segunda-feira, com um total de {segunda} votos!')
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print(f'O dia mais votado para a live foi terça-feira, com um total de {terca} votos!')
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print(f'O dia mais votado para a live foi quarta-feira, com um total de {quarta} votos!')
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print(f'O dia mais votado para a live foi quinta-feira, com um total de {quinta} votos!')
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print(f'O dia mais votado para a live foi sexta-feira, com um total de {sexta} votos!')
else:
    print(f'Houve empate no número de votos!')