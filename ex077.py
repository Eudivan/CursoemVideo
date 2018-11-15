
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')
p = 0
for c in palavras:
    print(f'\nNa palvra \033[34m{c}\033[m temos ', end='')
    for letra in c:
        if letra in 'AEIOU':
            print(letra, end=' ')



