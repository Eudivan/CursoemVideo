pre = float(input('Qual o preço do produto? R$'))
des = (pre * 0.05)
pre2 = pre - des
print('O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f} '.format(pre, 5, pre2))
print('Você está economizando R${:.2f}'.format(des))