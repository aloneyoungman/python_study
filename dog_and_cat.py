from class_method import Animals

class Dog(Animals):
    def Round(self):
        print(f"{self.name} сделал кувырок")

    def Voice(self,):
        voice=lambda:f"{self.name} сказал гав"
        print(voice())

class Cat(Animals):
    def Sleep(self,time: int):
        print(f"{self.name} лег спать на {time} минут")

    def Voice(self,):
        voice=lambda:f"{self.name} сказал мяу"
        print(voice())

dog=Dog("DOG","yes","blue",10,15)
dog.Round()
cat=Cat("Cat","yes","blue",10,15)
cat.Sleep(10)
dog.Voice()


bally=Dog("Bally","no","green",20,15)
brany=Dog("Brany","no","black",13,31)
bars=Dog("Bars","no","white",5,1)
dogs=[bally,brany,bars]

matilda=Cat("Matilda","yes","orange",3,3)
musya=Cat("Musya","no","redhead",6,6)
simba=Cat("Simba","yes","burgundy",666,666)
cats=[matilda,musya,simba]

for cat in cats:
    cat.Voice()

for dog in dogs:
    dog.Voice()
