print("Введите число от 1 до 9...")
x = int(input())
if 1<=x<=3:
    print("Введите строку...")
    s = input()
    print("Введите число повторов строки...")
    n = int(input())
    i = 0
    while i <= n:
        print(s)
        i = i + 1
elif 4<=x<=6:
    print("Введите степень возведения числа...")
    m = int(input())
    a = x**m
    print(a)
elif 7<=x<=9:
    i = 1
    while i <= 10:
        print(x)
        i = i + 1
        x = x + 1
else:
    print("Ошибка ввода!!!")