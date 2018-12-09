aluno = {}
aluno['nome'] = str(input('Nome do aluno: ')).strip().capitalize()
aluno['média'] = float(input('Digite a média: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('\n´´´´´´´´´´´´´´´´´´´')
for k, v in aluno.items():

    print(f'{k} = {v}')

