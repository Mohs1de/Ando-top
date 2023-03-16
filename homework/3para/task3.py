summas1 = int(input('введите сумму первого товара:'))
summas2 = int(input('введите сумму второго товара:'))
summas3 = int(input('введите сумму третьего товара:'))
if summas1 <= summas2 and summas2 <= summas3:
    print('Акция!')
    print('К оплате:', (summas1 + summas2 + summas3)//2)
elif summas3 <= summas2 and summas2 <= summas1:
    print('Акция!')
    print('К оплате:', (summas1 + summas2 + summas3)//3)
else:
    print('К оплате:', summas1 + summas2 +summas3)