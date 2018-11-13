alt = float(input('Digite a altura: (m) '))
pes = float(input('E o peso? (Kg) '))

imc = pes / alt ** 2

print('Com altura {:.2f}m e peso de {:.1f}Kg seu IMC é {:.1f}! Seu status é...'.format(alt, pes, imc))
if imc < 18.5:
    print('Abaixo do peso!')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso!')
elif imc <= 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')
