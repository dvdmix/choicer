import random
while True:
    n = int(input("Введите количество элементов: "))
    j = int(input("Сколько вернуть: "))
    list = []
    if j > n or j<1 or n<1:
        print("Такого не бывает.")
        continue
    for i in range(0,n):
        a = input("Введите значение: ")
        list.append(a)
    if j==1:
        b = random.choice(list)
    elif j>1:
        d = random.sample(list, j)
        b = ', '.join(d)
    print(b)
    print("Продолжить? 1 - да, 2 - нет.")
    c = int(input())
    if c == 1:
        continue
    elif c == 2:
        break
    else:
        print("чё")