nome1 = str(input('seu nome completo: ')).strip()
nome = nome1.split()
print('Muito prazer em te conhecer!')
print('seu primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))
