print('''-----------
  TABUADA
-----------\n\n''')
n = total = 0
while True:
    n = int(input('Tabuada de qual número você quer ver? '))
    if n < 0:
        break
    for c in range(1, 11):
        total = n * c
        print(f'{n:1} X {c:1} = {total:1}')
    print('-------------------------')
print('\n\nPrograma encerrado!')