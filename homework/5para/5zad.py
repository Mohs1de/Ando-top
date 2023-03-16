nomer = input("Введите числа:")
nomer = [int(x) for x in nomer.split()]
length = len(nomer)
if length == 1:
    print("Нет")
elif nomer == list(range(nomer[0], nomer[-1] + 1)):
    print("Да")
else:
    print("Нет")