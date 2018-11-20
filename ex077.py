
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')
p = 0
for c in sorted(palavras):
    print(f'\nNa palvra \033[34m{c}\033[m temos ', end='')
    for letra in c:
        if letra in 'AEIOU':
            print(letra, end=' ')


# SEGUNDO CÓDIGO

print('\n\n\n\n')
p = ('gato cachorro brigadeiro carro navio barco aviao martelo camisa dado mochila livro arvore bicicleta machado'
     'pedra foto pintura casa cebola pizza sorvete ventilador peru goiaba banana uva ovo homem mulher').split( )

for pala in sorted(p):
    print(f'\nNa palavra {pala.upper()} temos ', end='')
    for l in pala:
        if l in 'aeiou':
            print(l.upper(), end=' ')


