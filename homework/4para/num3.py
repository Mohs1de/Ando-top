loger = input('введите логин:\n').lower()
passworder = '=?*^$№@_'
choto = ''
for i in loger:
    for x in passworder:
        if i == x:
            choto += x
print(choto)