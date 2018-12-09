from datetime import datetime
dicio = {}
dicio['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
dicio['idade'] = datetime.today().year - ano
while True:
    ctps = str(input('Tem Carteira de Trabalho? [s/n] ')).strip().lower()
    if ctps in 'sn':
        break
if ctps == 's':
    dicio['ctps'] = int(input('Digite o numero da sua Carteira de Trabalho: '))
    dicio['salário'] = float(input('Informe o salário: '))
    anodecon = int(input('Ano de contratação: '))
    dicio['ano de contratação'] = anodecon
    aposenta = 35 - (datetime.today().year - anodecon) + dicio['idade']
for k, v in dicio.items():
    print(f'  -- {k}: {v}')
if ctps == 's':
    print(f'ira se aposentar com {aposenta} anos de idade.')


