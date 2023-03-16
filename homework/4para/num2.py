number = 5
BOR = input('введите (game), если хотите перейти в раздел развлечений, (off - завершить)\n').lower()
if BOR == 'game':
    print('запущена игра угадай число')
    while True:
        tru = int(input('введите число:'))
        if tru == number:
            print('Вы выиграли билеты на концерт!')
            break
        elif tru is not number:
            print('попробуйте еще раз:')
if BOR == 'off':
    print('пока, пока!')