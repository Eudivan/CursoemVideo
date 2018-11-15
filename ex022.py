nom = str(input('Seu nome completo: ')).strip()
print(len(nom))
prnom = nom.split()[0]
print('seu nome em maiusculo é {}'.format(nom.upper()))
print('seu nome em minusculo é {}'.format(nom.lower()))
print('seu nome completo tem {} letras'.format(len(nom) - nom.count(' ')))
print('seu primeiro nome {} tem {} letras.'.format(prnom.capitalize(), len(prnom)))

