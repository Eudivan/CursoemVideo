dia = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Qual a quantidade de Km percorridos? Km '))
val = dia * 60 + km * 0.15
print('O valor a paga é R${:.2f} mais a taxa por quilomentro rodado de R${:.2f} \n TOTAL  = R${:.2f}'
      .format((dia * 60), (km * 0.15), val))
