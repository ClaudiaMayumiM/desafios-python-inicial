''' 
DESAFIO:

Na língua inglesa existem algumas métricas de legibilidade, que podem ser calculadas automaticamente a partir de um texto. O objetivo dessas métricas é classificar a dificuldade de leitura do texto e indicar qual o nível de instrução e idade que o leitor deve ter para compreender bem o texto. Essas métricas são úteis para reescrever um texto até que ele fique mais acessível.

Uma dessas métricas é a Automated readability index, que pode ser calculada a partir da seguinte fórmula:

4.71 * (quantidade de letras / quantidade de palavras) + (quantidade de palavras / quantidade de frases) - 21.43

Seu objetivo neste desafio é escrever uma função simplificada para calcular o automated readability index. O resultado da fórmula deve ser arredondada para o próximo inteiro e seu valor máximo deve ser 14. Se o resultado da fórmula for, 10.4, por exemplo o retorno da função deve ser 11.


'''

import math

# sentence = 'And you may ask yourself Well how did I get here'

sentence = 'The latter consisted simply of six hydrocoptic marzelvanes so fitted to the ambifacient lunar waneshaft that side fumbling was effectively prevented'

def word_counter(sentence):
  
  global word_list
  word_list = sentence.split()

  word_count = 0

  for word in word_list:
    word_count += 1

  return word_count


def letter_counter(word_list):

  letters_str = "".join(word_list)

  letter_count = len(letters_str)

  return letter_count



def automated_readability_index(sentence):
  
  word_num = word_counter(sentence)
  letter_num = letter_counter(word_list)

  first_part = 4.71 * letter_num / word_num

  second_part = 0.5 * word_num

  final_result = round(first_part + second_part - 21.43, 2)

  final_result = math.ceil(final_result)

  if final_result > 14:
    return 14

  return final_result



print(automated_readability_index(sentence))