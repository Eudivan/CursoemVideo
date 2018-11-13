media = 0
m20 = 0
idade = 0
nome = 0
ano = 'ano'
for p in range(1, 5):
    print('----{}ª PESSOA-----'.format(p))
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().upper()
    media += i
    if s == 'F' and i < 20:
        m20 += 1
    if s == 'M' and i > idade:
        idade = i
        nome = n
print('A idade média do grupo é {}'.format(media/4))

if m20 == 0:
    print('Não tem mulheres com menos de 20 anos nesse grupo!')
elif m20 == 1:
    print('Apenas uma mullher têm menos que 20 anos')
else:
    print('Tem {} mulheres menores de vinte anos'.format(m20))
if idade != 1:
    ano = 'anos'

if idade > 0:
    print('O homem mais velho é o {} com {} {}!'.format(nome, idade, ano))
else:
    print('Não tem homens nesse grupo!')
