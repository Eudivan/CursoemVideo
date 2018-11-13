sexo = str(inpFut('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Opção inválida! Informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
