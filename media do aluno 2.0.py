nome  = str(input('Digite aqui o nome completo do aluno: \n >>>'))
idade = int(input(f'Qual a idade de {nome}: \n >>>'))
id = '0462584'

print(f'Encontrado: \n Nome: {nome} \n Idade: {idade} \n ID do Aluno: {id} \n')

n1 = float(input(f'Digite a nota de Portguês do aluno {nome} [{id}]: \n >>>'))
n2 = float(input(f'Digite a nota de Matemática do aluno {nome} [{id}]: \n >>>')
n3 = float(input(f'Digite a nota de Química do aluno {nome} [{id}]: \n >>>'))
n4 = float(input(f'Digite a nota de História do aluno {nome} [{id}]: \n >>>'))
n5 = float(input(f'Digite a nota de Geografia do aluno {nome} [{id}]: \n >>>'))
n6 = float(input(f'Digite a nota de Física do aluno {nome} [{id}]: \n >>>'))
n7 = float(input(f'Digite a nota de Inglês do aluno {nome} [{id}]: \n >>>'))
n8 = float(input(f'Digite a nota de Artes do aluno {nome} [{id}]: \n >>>'))
n9 = float(input(f'Digite a nota de Ed. Física do aluno {nome} [{id}]: \n >>>'))
n10= float(input(f'Digite a nota de Espanhol do aluno {nome} [{id}]: \n >>>'))

media = [(n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10) / 5]

print(f'Com as notas fornecidas, a média do aluno {nome} de {idade} anos é {media}')

if media >= 6:
	print(f'\n{nome} foi APROVADO com SUCESSO!\n')
elif media == 5:
	print(f'\n{nome} foi aprovado, mas pode melhorar\n')
elif media <= 4:
	print(f'\n{nome} foi REPROVADO, precisa se empenhar mais\n')

