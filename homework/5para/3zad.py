ando = [0, 0, 0, 0, 0]
gamo = int(input("Введите значение: "))

while ando != -1:
    gamo[ando - 1] += 1
    ando = int(input("введите значение: "))

percent = ando[-1] / sum(ando) * 100
print("Percent of 5's is %s" % int(percent) + '%')