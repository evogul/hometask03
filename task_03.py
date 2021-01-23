'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
исправлено
'''
def my_func(num1, num2, num3):
    min_num = min(num1, num2, num3)
    if min_num == num1:
        return num2 + num3
    elif min_num == num2:
        return num1 + num3
    else:
        return num + num2

num1 = int(input('введите первое число: '))
num2 = int(input('введите второе число: '))
num3 = int(input('введите третье: '))
print(f'сумма двух наибольших чисел : {my_func(num1, num2, num3)}')