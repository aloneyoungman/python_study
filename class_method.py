# Лучше сначала описать все функции/классы, а потом уже код
# Иначе всё идёт в разнобой и это тяжело читать
#
# Также на будущее прошу писать "документацию" для классов и функций (https://www.programiz.com/python-programming/docstrings)
# В питоне это делается просто:
def exampleFunc():
    '''
    Здесь будет записано описание функции.
    Если я наведу на неё мышку - увижу подсказку
    '''
    # Здесь начинается тело функции
    return True
#

a1=[1,2,"a","2"]
a2=(1,2,"a","2")
a3="dsfer4"

def GetOnlyEven(spisok: list)->list:
    if type(spisok)==list:
        spisok_new=[]
        for i in range(len(spisok)):
            if i%2==0:
                spisok_new.append(spisok[i])
        return spisok_new
    else:
        return "ArgumentError"
    

print(GetOnlyEven(a1))
print(GetOnlyEven(a2))
print(GetOnlyEven(a3))


b1="sdfkjhwei34"
b2=(3,2,2)
b3=["weqweq"]

# Все блоки стоит отделять пустой строкой
# Ниже ты вызываешь print сразу после метода
# Стоит добавить хотя бы одну строку отступа
def OrderString(string: str)->str:
    if type(string)==str:
        return "".join(sorted(string))
    else:
        return "ArgumentError"
print(OrderString(b1))
print(OrderString(b2))
print(OrderString(b3))



class Animals:
    # Здесь начались проблемы
    # Метод init - констуктор класса.
    # Т.е. он вызывается, когда мы пытаемся создать объект класса
    # В данном случае это строка типа "var = Animals()"
    # Т.е. мы создали конкретный объект (конкретное животное)
    # 
    # так как мы хотим работать с конкретным животным - мы хотим чтобы он обладал конкретными характеристиками
    # Их стоит получить при инициализации из параметров (точно также как ты получил имя)
    # Так же стоит сделать для остальных свойств объекта
    #
    # Для случаев, когда, какое - то свойство можно указать, а можно и не указывать
    # существуют значения по умолчанию (https://www.geeksforgeeks.org/default-arguments-in-python/)
    #
    # Метод set_age() - если добавляешь функциональность без задания - просьба оставлять 
    # хотя бы небольшой коммент, чтобы было понятно
    #

    def __init__(self,name):
        self.name=name
        self.IsPredator=True
        self.__age=1
        self.color="blue"
        self.weight=10
        self.height=10

    def set_age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    def get_age(self):
        return self.__age


    def Walk(self,sec: int):
        if type(sec)==int:
            print(f"{self.name} прошел {sec*(10/self.weight)}")
        else:
            print("ArgumentError")

    def GetIMT(self):
        return self.weight/(self.height**2)

    def Voice(self):
        print(f"Меня зовут {self.name}")

def GetAnimalColor(Animal):
    if isinstance(Animal, Animals):
        return Animal.color
    else:
        return "ArgumentError"

bear=Animals("qwe")
bear.set_age(-20)
bear.set_age(20)
print(bear.get_age())
bear.Walk(20)
print(bear.GetIMT())
bear.Voice()
print(GetAnimalColor(bear))

