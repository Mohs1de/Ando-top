price = int(input('сумма к оплате:'))
timer = int(input('укажите время:'))

if 8 <= timer <=22:
    if 10 <= timer <= 12:
        print(price//2)
    if 20 <= timer <= 22:
        print(price//4)
else:
    print('Магазин закрыт!')