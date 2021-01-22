'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов
'''
def my_func(num1, num2, num3):
    return max(num1, num2, num3)

num1 = int(input('input first number: '))
num2 = int(input('input second number: '))
num3 = int(input('input third number: '))
print(f'maximum is: {my_func(num1, num2, num3)}')