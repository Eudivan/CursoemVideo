from emoji import emojize
from time import sleep
print('Presione \033[33;1mENTER\033[m para iniciar!')
ok = input('')
for contador in range(10, -1, -1):
    print(contador)
    sleep(1)
print(emojize('\033[33m:fireworks: :fireworks: :fireworks: :fireworks: :fireworks::fireworks::fireworks::fireworks::fireworks:'
              ':fireworks: :fireworks: :fireworks: :fireworks: :fireworks: :fireworks:'))
sleep(0.5)
print(emojize('\033[32m:fireworks: :fireworks: :fireworks: :fireworks: :fireworks::fireworks::fireworks::fireworks::fireworks:'
              ':fireworks: :fireworks: :fireworks: :fireworks: :fireworks: :fireworks:'))
sleep(0.4)
print(emojize('\033[31m:fireworks: :fireworks: :fireworks: :fireworks: :fireworks::fireworks::fireworks::fireworks::fireworks:'
              ':fireworks: :fireworks: :fireworks: :fireworks: :fireworks: :fireworks:'))
sleep(0.2)
print(emojize('     \033[33m:fireworks::fireworks:\033[34;1mFELIZ ANO NOVO!:fireworks::fireworks:\033[m'))
print(emojize('\033[30m:fireworks: :fireworks: :fireworks: :fireworks: :fireworks::fireworks::fireworks::fireworks::fireworks:'
              ':fireworks: :fireworks: :fireworks: :fireworks: :fireworks: :fireworks:'))
sleep(0.4)
print(emojize('\033[34m:fireworks: :fireworks: :fireworks: :fireworks: :fireworks::fireworks::fireworks::fireworks::fireworks:'
              ':fireworks: :fireworks: :fireworks: :fireworks: :fireworks: :fireworks:'))
sleep(0.3)
print(emojize('\033[1m:fireworks: :fireworks: :fireworks: :fireworks: :fireworks::fireworks::fireworks::fireworks::fireworks:'
              ':fireworks: :fireworks: :fireworks: :fireworks: :fireworks: :fireworks:'))
