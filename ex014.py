tem = float(input('Informe a temperatura em ºC: '))
fah = tem * 1.8 + 32
kel = (fah + 459.67) / 1.8
print('A temperatura de {}°C corresponde a \n{}F \n{:.2f}K'.format(tem, fah, kel))
