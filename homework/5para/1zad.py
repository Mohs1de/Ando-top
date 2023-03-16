stolgame = input('введите настольную игру:\n').lower()
spit = []
while stolgame != '0':
    if stolgame not in spit:
        spit.append(stolgame)
    else:
        print('эта игра уже записана')
    stolgame = input()