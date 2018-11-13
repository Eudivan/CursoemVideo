mult = int(input('digite o numero que você quer ver os multiplos: '))
val = int(input('O programa vai mostra e somar de 0 a ... '))

print('Todos os múltiplo de ÍMPARES {} entre 0 e {} somados'.format(mult, val))
cont = 0
soma = 0
for mul in range(mult, val, mult):
    n1 = mul % 2
    if n1 == 0: #ESSE IF É QUEM RETIRA OS NÚMEROS PARES
        soma -= mul
        cont += 1

    soma = soma + mul

print('_____')
print('a soma dos {} é {}'.format(cont, soma))
