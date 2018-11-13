from math import hypot
co = float(input('digite o comprimento do cateto oposto: '))
ca = float(input('digite o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('a hipotenusa é {:.2f}'.format(hi))
