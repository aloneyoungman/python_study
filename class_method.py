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

def OrderString(string: str)->str:
    if type(string)==str:
        return "".join(sorted(string))
    else:
        return "ArgumentError"
print(OrderString(b1))
print(OrderString(b2))
print(OrderString(b3))



class Animals:
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

bear=Animals("BEAR")
bear.set_age(-20)
bear.set_age(20)
print(bear.get_age())
bear.Walk(20)
print(bear.GetIMT())
bear.Voice()
print(GetAnimalColor(bear))