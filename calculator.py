import numbers
def repeat_while_accept():
    print('Введите первое число: ')
    while True:
        a = input()
        if a.isdigit():
            break
        else:
            print('Вы ввели не число. Попробуйте ещё раз')

    print('Введите арифметическую операцию: "+","-","*","/" или "^"')
    while True:
        operator = input()
        if operator in ('+','-','*','/','^'):
            break
        else:
            print('Вы ввели неверное букву. Попробуйте ещё раз')
    print('Введите второе число ')
    while True:
        b = input()
        if float(b).is_integer():
            break
        else:
            print('Вы ввели неверное букву. Попробуйте ещё раз')
    return [a,operator,b]
list1=repeat_while_accept()
try:
    if list1[1]=="*":
        print(round(float(list1[0])*float(list1[2]),5))
    elif list1[1]=="/":
        print(round(float(list1[0])/float(list1[2]),5))
    elif list1[1]=="+":
        print(round(float(list1[0])+float(list1[2]),5))
    elif list1[1]=="-":
        print(round(float(list1[0])-float(list1[2]),5))
    elif list1[1]=="^":
        print(round(float(list1[0])**float(list1[2]),5))
except ZeroDivisionError:
    print("Попытка деления числа на ноль")
