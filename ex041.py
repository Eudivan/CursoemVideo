from datetime import date
from time import sleep
ano = int(input('Digite o ano de nascimento: '))
ida = date.today().year - ano

print('\033[1;34mO atleta tem {} anos! e sua categoria é...\033[m'.format(ida))
sleep(0.35)
if ida > 25:
    print('\033[33mMASTER!')
elif ida <= 9:
    print('\033[33mMIRIM!')
elif ida <= 14:
    print('\033[33mINFANTL!')
elif ida <= 19:
    print('\033[33mJUNIOR!')
elif ida <= 25:
    print('\033[33mSÊNIOR!\033[m')
