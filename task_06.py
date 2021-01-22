'''
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()
'''
def int_func(word):
    #первый способ
    return word.title()

def int_func_ord(word):
    #второй способ
    return chr(ord(word[0])-32)+word[1:]

error = False
txt = input('input text: ').split()
txt2 = txt.copy()
for word in txt:
    for i in range(len(word)):
        if 'abcdefghijklmnopqrstuvwxyz'.find(word[i])==-1:
            error = True
            break
    txt[txt.index(word)] = int_func(word)       #первый способ - используя встроенную функцию title
    txt2[txt2.index(word)] = int_func_ord(word) #второй способ - используя встроенную функцию ord
    if error == True:
        break
if error == True:
    print('Ошибка: слова в тексте должны содержать только латинские буквы')
else:
    print('Решение первым способом : '+' '.join(txt))
    print('Решение вторым способом (ord): ' + ' '.join(txt2))