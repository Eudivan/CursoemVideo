cont = soma = 0
print('Para encerrar digite 999')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} valores \nA soma entre eles é {soma}')
