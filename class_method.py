
def GetOnlyEven(spisok: list)->list:
    '''
    :param spisok:
    :return:
    '''
    if type(spisok)==list:
        spisok_new=[]
        for i in range(len(spisok)):
            if i%2==0:
                spisok_new.append(spisok[i])
        return spisok_new
    else:
        return "ArgumentError"


def OrderString(string: str)->str:
    if type(string)==str:
        return "".join(sorted(string))
    else:
        return "ArgumentError"


class Animals:
# В целом всё верно, но значения типа bool(IsPredator) - стоит передавать не строкой
# А именно предназначенным для этого значением (True\False)

    def __init__(self,name: str,IP: str,color: str,
                 weight: int, height: int):
        self.name=name

# Конструкцию ниже - можно упростить:
# У тебя идёт проверка "Если IP равно 'yes' тогда записать True, иначе записать False"
# Это же можно записать по другому и чуть более правильно:
# IsPredator равен условию IP == 'yes'
# т.к. IP == yes возращает значение типа bool - можно его сразу и записать
#
# т.е. так:
# self.IsPredator = (IP =='yes')
        if IP=="yes":self.IsPredator=True
        else: self.IsPredator=False
        self.__age=1
        self.color=color
        self.weight=weight
        self.height=height

    def set_age(self, age):
        """
        добавил метод set_age для того, чтобы можно было исключить ввод
        некорректного возраста ( то есть отрицательного ). Артибут
        self.__age является приватным и вызввать его можно только находясь
        находясь в этом классе, поэтому использую фильтр set_age, который
        при нужных нам условиях вызывает self.__age (Пардон за кривость
        описания, буду учиться это делать понятным языком)
        :param age:
        :return:
        """
# Всё отлично!
# Грамотный ход мыслей
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

#создаем разного типа аргументы для проверки метода GetOnlyEven
#который принимает список и возвращает список с четными позициями прнятого списка
spisok1=[1,2,3,"3","2","ert"]
spisok2={2:3,"r":3,6:"g"}
spisok3="fwef34"
spisok4=124

#вызываем метод GetOnlyEven
print(GetOnlyEven(spisok1))
print(GetOnlyEven(spisok2))
print(GetOnlyEven(spisok3))
print(GetOnlyEven(spisok4))

#то же самое делаем для метода OrderString,
#который возвращает строку с отсортированными по алфавиту символами
string1=[1,2,3,"3","2","ert"]
string2={2:3,"r":3,6:"g"}
string3="fwef34"
string4=124

print(OrderString(string1))
print(OrderString(string2))
print(OrderString(string3))
print(OrderString(string4))


#создаем объект класса Animals
bear=Animals("BEAR","yes","blue",10,15)
lion=Animals("LION","yes","orange",25,10)
dog=Animals("CAT","no","blue",2,5)

bear.set_age(20)
lion.set_age(0)
dog.set_age(200)

print(bear.get_age())
print(lion.get_age())
print(dog.get_age())

bear.Walk(20)
lion.Walk(40)
dog.Walk(1000)

print(bear.GetIMT())
print(lion.GetIMT())
print(dog.GetIMT())

bear.Voice()
lion.Voice()
dog.Voice()


print(GetAnimalColor(bear))
print(bear.IsPredator)