# Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.

# Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas deve ser exibida uma mensagem no seguinte padrão:

# VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

# POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.


notas_impares = 0
notas_pares = 0

for aluno in range(1, 51, 2):
    print('Você está digitando as notas dos alunos ímpares.')
    valor_nota = float(input('Por favor, insira a nota do aluno de número {}: '.format(aluno)))
    notas_impares += valor_nota

for aluno in range(2, 51, 2):
    print('Você está digitando as notas dos alunos pares.')
    valor_nota = float(input('Por favor, insira a nota do aluno de número {}: '.format(aluno)))
    notas_pares += valor_nota

media_impares = notas_impares / 25
media_pares = notas_pares / 25

print('As médias foram: {} e {}, para as turmas ímpares e pares, respectivamente.'.format(media_impares, media_pares))

if media_impares > media_pares:
    print('Os alunos ímpares obtiveram a maior média, com valor de {}!'.format(media_impares))
elif media_pares > media_impares:
    print('Os alunos pares obtiveram a maior média, com valor de {}!'.format(media_pares))
else:
    print('Os valores das médias dos alunos pares e ímpares foram os mesmos, caracterizando um empate!')
