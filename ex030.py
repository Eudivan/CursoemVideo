from time import sleep
num = int(input('\033[1;10mdigite um número: \033[m'))
print('\033[34mO número {} é...\033[m'.format(num))
sleep(0.5)
if num / 2 % 1 == 0:
    print('\033[32mPAR')
else:
    print('\033[32mÍMPAR')
