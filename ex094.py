from time import sleep
pessoa = {}
lista = []
mulher = []
acima = []
m = 0

while True:
    pessoa['Nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        pessoa['Sexo'] = str(input('Sexo:[M/F] ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M p/ masculino ou F p/ feminino')
    pessoa['Idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    pessoa.clear()
    while True:
        m1 = str(input('Para adicionar outra pessoa tecle ENTER ou 0 para encerrar: '))
        if m1 in ' 0':
            break
    if m1 == '0':
        break


print('=-' * 30)


print(' - Total de pessoas cadastradas: ', len(lista))
for i in lista:
    m += i['Idade']
    if i['Sexo'] == 'F':
        mulher.append(i['Nome'])
        mulher.append(i['Idade'])

media = m // len(lista)
print(f' - A média de Idade de desse grupo é de {media} anos')
print('-' * 32)
print(f'      Total de mulheres: {len(mulher) // 2}')
print('-' * 32)
for i, m in enumerate(mulher):
    if i % 2 == 0:
        print(f'  Nome: {m} - ', end='')
    else:
        print(f'Idade = {m} anos')
print('-' * 32)
for c in lista:
    if c['Idade'] > media:
        acima.append(c['Nome'])
        acima.append(c['Idade'])

print('      Acima da idade média')
print('-' * 32)
for i, v in enumerate(acima):
    if i % 2 == 0:
        print(f'Nome: {v} - ', end='')
    else:
        print(f'Idade = {v} anos')
print('-' * 32)

print('.\n' * 10)
sleep(0.4)
print(lista)






