print('\033[34mTABUADA\33[m')
num = int(input('digite o numero para consltar a tabuada: '))
print('\033[34mAqui está a tabuada do {}'.format(num))
for tabuada in range(0, 11, 1):
    print('\33[33m{:2} X {:2} = {:2}\033[m'.format(num, tabuada, num * tabuada))
