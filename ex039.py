from datetime import date
ano = int(input('Seu ano de nascimento: '))
sex = str(input('''Digite M ou F:
[M] Masculino
[F] Feminino
''')).strip().lower()

ida = date.today().year - ano
print('quem nasceu em {} faz {} anos em {}!'.format(ano, ida, date.today().year))

if sex != 'f' and sex != 'm':
    print('Algo digitado errado! verifique seus dados e tente novamente')
elif sex == 'f':
    print('O alistameto é somente obrigatório para homens! você não precisa se alista.')
elif ida == 18:
    print('Você tem que se apresenta IMEDIATAMENTE!')
elif ida < 18:
    print('ainda falta {} anos para o alistamento\n Seu alistameto é em {}'.
          format(18 - ida, ano + 18))
elif ida > 18:
    print('Você deveria ter se alistado a {} anos atrás em {}!'.format(ida - 18, ano + 18))
