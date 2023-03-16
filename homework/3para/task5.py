number = input()
AYE = sum(map(int,str(number)))
if AYE % 3 == 0 and int(number[-1]) % 2 == 0:
    print('делится')
else:
    print('не делится')