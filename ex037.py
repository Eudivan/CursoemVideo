num = int(input('Digite o numero para converter: '))
print('''Digite: 
[1] para Binário 
[2] para Octal
[3] para Hexadecimal''')
boh = int(input('Sua opção: '))

if boh == 1:
    tipo = 'binário'
    n1 = bin(num)
elif boh == 2:
    tipo = 'octal'
    n1 = oct(num)
else:
    tipo = 'hexadecimal'
    n1 = hex(num)
print('O numero {} em {} é:\n{}'.format(num, tipo, n1[2:]))
