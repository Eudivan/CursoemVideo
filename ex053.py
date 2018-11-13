fra = str(input('Digite uma frase: ')).strip().upper()
frase = fra.replace(' ', '')
print('A frase "{}" invertida "{}" '.format(fra, fra[::-1]), end='')
palindromo = frase[::-1]
if frase == palindromo:
    print('\033[34mÉ UM PALÍNDROMO!\033[m')
else:
    print('\033[31mNÃO É UM PALÍNFROMO!\033[m')
