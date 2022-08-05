import emoji



import random

import math #importa todas as funcionalidades da blblioteca MATH
n = int(input("digite:"))
raiz = math.sqrt(n)
print("a raiz do numero {} é igual a {}".format(n, math.floor(raiz)))

nn = random.random() #usando a biblioteca RANDOM para gerar um numero randomico entre 0 e 1
                     #se quiser um numero inteiro, tem qusar RANDINT - random.randint
ninteiro = random.randint(1, 10) #define o primeiro e último número
print(nn)
print(ninteiro)
print('{} x {} = {}'.format(n, nn, (math.trunc(n * nn)))) #TRUNC retorna o numero truncado, sem arredondar, ex.: 4,7 -> 4, precisa importar a lib MATH
print(n*ninteiro)
print(emoji.emojize('python is :smirk:', language='alias')) #lib EMOJI para usar emojis