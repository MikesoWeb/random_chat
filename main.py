from random import choice
from colorama import Fore
import time
l = ['првиет, как дела?', 'хай, что нового?', 'хаюшки, как сам?']
random_user = ['Mike', 'Tom', 'Petr']

print(Fore.GREEN,'Добро пожаловать в рандомный чат!')
time.sleep(1)
print('Система выдаст вам случайного собеседника')
time.sleep(1)

print(f'Нажмите {Fore.RED}r{Fore.GREEN} чтобы начать чат. Нажмите {Fore.RED}q{Fore.GREEN} чтобы выйти.')
a = input('Введите команду: ')
print(f'Вы нажали {a}')
if a == 'q':
  print('До новых встреч.')

if a == 'r':
  
  d = choice(l)
  rnd_usr = choice(random_user)

  time.sleep(1)
  print(rnd_usr, ' пишет....')
  time.sleep(1)

  print(rnd_usr,':',Fore.CYAN, d)


