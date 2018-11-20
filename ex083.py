ex = str(input('Digite a expressão: ')).strip()
if ex.count('(') == ex.count(')') and ex[0] != ')' and ex[-1] != '(' and '()' not in ex and ')(' not in ex:
    print('A expressão esta correta!')
else:
    print('A expressão está errada!')


