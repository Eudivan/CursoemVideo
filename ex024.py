city = str(input('digite o nome da cidade: ')).strip().capitalize()
print('Você digitou ', city)
if city.find('Santo'):
    print('não tem Santo no começo.')
else:
    print('tem Santo no começo.')
