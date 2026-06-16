import time

name = input('ты Мирас ? ')
if name.lower() == 'гуль':
    number = 1000
    while number > 0:
        print(f'{number}-{7}')
        time.sleep(0.1)
        number -= 7
    print(0)
else:
    print('ты не Мирас') 
