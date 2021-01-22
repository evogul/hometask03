'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
def num_division(num1, num2):
    if num2==0:
        print('Devision by zero')
        return None
    else:
        return num1 / num2

num1 = int(input('input first number: '))
num2 = int(input('input second number: '))
result = num_division(num1, num2)
if result!=None:
    print(result)