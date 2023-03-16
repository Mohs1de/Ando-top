z = ('введите отзыв (off - завершить)')
print(z)
while True:
    feedback = input()
    if feedback == 'off':
        break
    print('Спасибо, ваш отзыв принят!')
print('Система предпочтений настроена!')