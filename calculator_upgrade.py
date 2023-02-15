def repeat_while_accept():
    print('Введите первое число: ')
    while True:
        b = input()
        if b.isdigit():
            break
        else:
            print('Вы ввели неверное букву. Попробуйте ещё раз')

    print('Введите букву q,w или e')
    while True:
        operator = input()
        if operator in ('+','-','*','/','^'):
            break
        else:
            print('Вы ввели неверное букву. Попробуйте ещё раз')
    print('Введите букву q,w или e')
    while True:
        b = input()
        if b.isdigit():
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



