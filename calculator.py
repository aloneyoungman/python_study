try:
    a=float(input("Введите первое число"))
    o=str(input("Введите любую из операций: *,/,+.-,^"))
    if o!="/" and o!="*"and o!="+" and o!="-" and o!="^":
        raise Exception("Вы ввели некорректный символ арифметической операции")
    b=float(input("Введите второе число:"))
    if o=="*":
        print(round(a*b,5))
    elif o=="/":
        print(round(a/b,5))
    elif o=="+":
        print(round(a+b,5))
    elif o=="-":
        print(round(a-b,5))
    elif o=="^":
        print(round(a**b,5))

except ValueError:
        print("Преобразование прошло неудачно")
except ZeroDivisionError:
    print("Попытка деления числа на ноль")
except BaseException:
    print("Вы ввели некоректный символ арифметической операции")
print("Завершение программы")