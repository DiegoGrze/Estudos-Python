import random
aluno1 = str(input('Nome do primeiro aluno:'))
aluno2 = str(input('Nome do segundo aluno:'))
aluno3 = str(input('Nome do terceiro aluno:'))
aluno4 = str(input('Nome do quarto aluno:'))
lista = [aluno1,aluno2,aluno3,aluno4]
#random.choice faz a escolha aleatória no vetor LISTA
escolhido = random.choice(lista)
print('o aluno escolhido randomicamente foi {}'.format(escolhido))
#para mostrar o Vetor inteiro aleatoriamente, usa-se random.shuffle
random.shuffle(lista)
print('Essa é a lista dos alunos cadastrados, mostrada aleatoriamente', (lista))