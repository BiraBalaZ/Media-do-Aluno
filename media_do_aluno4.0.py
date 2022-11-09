import pandas as pd
import numpy as np
import random

#Coletando nome e idade do aluno
nome   = str(input('Digite aqui o primeiro nome do aluno: \n >>>'))
idade  = int(input(f'\n Qual a idade de {nome}: \n >>>'))
altura = float(input(f'\n Qual a altura de {nome}: \n >>>'))
peso   = float(input(f'\n Qual o peso de {nome}: \n >>>'))

#Gerando um ID entre 100 mil e 999 mil
id = random.randint(100000, 999999)

#Fórmula do IMC
imc = int(peso / (altura**2))

#Variaveis da colunda
coluna = 'Dados'.split()
linha  = 'Nome Idade Altura Peso ID IMC'.split()
dados  = f'{nome} {idade} {altura} {peso} {id} {imc}'.split()

#Criando a tabela
tabela = pd.DataFrame(data = dados, index = linha, columns = coluna)

#Printando a tabela depois de coletar os dados do usuário
print(f'\n{tabela}')

#Exibindo mensagem de acordo com o IMC do Aluno
if imc < 18.5:
	print(f'\n{nome} está abaixo do peso. \n')
elif imc >= 18.5 and imc <= 24.99:
	print(f'\n{nome} está com peso normal. \n')
elif imc >= 25.0 and imc <= 29.99:
	print(f'\n{nome} está acima do peso. \n')
elif imc >= 30.0:
	print(f'\n{nome} está muito acima do peso. \n')

#Coletando as notas de cada matéria do aluno
n1 = float(input(f'Digite a nota de Portguês do aluno {nome}      \n >>>'))
n2 = float(input(f'\nDigite a nota de Matemática do aluno {nome}  \n >>>'))
n3 = float(input(f'\nDigite a nota de Química do aluno {nome}     \n >>>'))
n4 = float(input(f'\nDigite a nota de História do aluno {nome}    \n >>>'))
n5 = float(input(f'\nDigite a nota de Geografia do aluno {nome}   \n >>>'))
n6 = float(input(f'\nDigite a nota de Física do aluno {nome}      \n >>>'))
n7 = float(input(f'\nDigite a nota de Inglês do aluno {nome}      \n >>>'))
n8 = float(input(f'\nDigite a nota de Artes do aluno {nome}       \n >>>'))
n9 = float(input(f'\nDigite a nota de Ed. Física do aluno {nome}  \n >>>'))
n10= float(input(f'\nDigite a nota de Espanhol do aluno {nome}    \n >>>'))

#Somando as notas e dividindo por 10, para ter a média do aluno
media = float((n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10) / 10)

#Imprimindo o nome, idade e média baseada no cálculo acima
print(f'\nCom as notas fornecidas, a média do aluno {nome} de {idade} anos é {media:.2f}')

#Se a média for 6 ou acima, ele passou;
#Se a média for 5 ele passou, mas precisa melhorar;
#Se a média for 4 ou abaixo, ele reprovou.
if media >= 6.0 and media <= 10:
	print(f'{nome} foi APROVADO com SUCESSO! \n')
elif media == 5.0:
	print(f'{nome} foi aprovado, mas pode melhorar \n')
elif media <= 4.0 and media >= -5.0:
	print(f'{nome} foi REPROVADO, precisa se empenhar mais \n')
else:
    print('[ERROR 001] Erro desconhecido, favor contatar o Dev encarregado')
