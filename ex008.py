m = float(input('Digite a distância em metros: '))
print('a medida de {:.1f}m corresponde a \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'
      .format(m, (m / 1000), (m / 100), (m / 10), (m * 10), (m * 100), (m * 1000)))
