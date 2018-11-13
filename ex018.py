from math import sin, cos, tan, radians
ang = float(input('Digite um angulo: °'))
angX = radians(ang)
print('O ângulo de {}° tem o\nSENO de {:.2f}'.format(ang, sin(angX)))
print('COSSENO de {:.2f}'.format(cos(angX)))
print('TANGENTE de {:.2f}'.format(tan(angX)))
print('\n {}° em radianos é {:.2f}'.format(ang, angX))