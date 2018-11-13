fra = str(input('Digite a frase: ')).strip().lower()
print('a frase tem {} letras "a"'.format(fra.count('a')))
print('A letra "a" apareceu na posiçao {} \nA letra "a" apareceu por ultimo na posição {}'.format(fra.find('a')+1, fra.rfind('a')+1))
