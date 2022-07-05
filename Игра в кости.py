import time
import random
print('Вас приветсвует приложение для игры в кости')
a=int(input('1-Просто кинуть кубик, 2-игра против ИИ'))
if a==1:
    print('Хорошо, играем!')
    print('Идёт бросок:')
    for seconds in range(1,4):
        print(seconds)
        time.sleep(1)
    brosok=random.randrange(1,6)
    print('ВЫ КИНУЛИ:',brosok)
elif a==2:
    print('Вы кинули вызов роботу!')
    time.sleep(1)
    print('Ладно...')
    time.sleep(1)
    print('Вы первый кидаете кубик...')
    time.sleep(1)
    brosok=random.randrange(1,6)
    print('ВЫ КИНУЛИ:',brosok)
    time.sleep(1)
    print('Теперь кидает робот...')
    time.sleep(1)
    brosok2 = random.randrange(1,6)
    print('ЕМУ ВЫПАДАЕТ:',brosok2)
    time.sleep(1)
    while brosok == brosok2:
        print('ПЕРЕБРОС!')
        time.sleep(1)
        brosok=random.randrange(1,6)
        print('ВЫ КИНУЛИ:',brosok)
        time.sleep(1)
        print('Теперь кидает робот...')
        time.sleep(1)
        brosok2 = random.randrange(1,6)
        print('ЕМУ ВЫПАДАЕТ:',brosok2)
        time.sleep(1)
        while brosok == brosok2:
            break

    if brosok>brosok2:
        print('ВЫ ПОБЕДИЛИ!')
    elif brosok<brosok2:
        print('ВЫ ПРОИГРАЛИ!')
else:
    print('Ошибка, введите корректную команду')




