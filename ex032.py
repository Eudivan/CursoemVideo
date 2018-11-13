from datetime import date
ano = int(input('\033[1;34mDIGITE O ANO:\033[mpara o ano atual digite 0 '))
if ano == 0:
    ano = date.today().year
print('O ano {} '.format(ano))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('é Bissexto!')
else:
    print('nâo é bissexto!')
