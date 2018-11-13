from time import sleep
print('\033[34m~~' * 11)
print('  Finaciamento casa')
print('~~' * 11 + ' \033[m ')

sal = float(input('Informe seu salário: R$'))
cas = float(input(' Informe o valor da casa: R$'))
ano = float(input('Em quantos anos você pretende parcelar? '))

print('\033[1;10mO seu pedido foi...\033[m')
sleep(1)

mes = ano * 12
parc = cas / mes
tri = sal * 0.3
if parc <= tri:
    print('\033[33mAPROVANDO!')
    print('O Você parará {:.0f} parcelas de R${:.2f}\033[m'.format(mes, parc))
else:
    print('\033[31mNEGADO!')
    print('Infelimente seu finaciamento não pode ser liberado, pois o valor da parcela de R${:.2f} é superior a 30% do seu sálario\033[m'.format(parc))
print('Para pegar uma casa no valor R${:.2f} em {:.0f} anos é necessário que a parcela seja igual ou inferior a 30%'.format(cas, ano))
