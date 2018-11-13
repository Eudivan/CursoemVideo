lar = float(input('digite a largura: '))
alt = float(input('digite a altura: '))
area = lar * alt
print('Sua parede tem a dimensão de {}x{} e sua área é {}m².'.format(lar, alt, area))
tin = area / 2
print('para pintar essa parede, você precisará de {}l de tinta.'.format(tin))
