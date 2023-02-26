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

# Здесь опять обращаю внимание, что булевские значения надо передавать через True\False, а не строкой 'yes'\'no'
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

# Здесь я имел ввиду следующее:
# Создать список из обоих объектов (т.е. чтобы в одном списке были и коты и собаки)
cats_and_dogs = list[Animals](cats+dogs)

# И сделать вызов метода Voice через общий метод
# примерно так:
def test_f(l:list[Animals]):
    for animal in l:
        animal.Voice()

test_f(cats_and_dogs)


# Таким образом мы обращаемся к методу класса, через наследование от Animals
# Но при этом можем обратиться и через конкретный класс
# Посмотри на подсказки, как компилятор определяет тип переменной в каждом случае (наведи мышку на переменную)
def other_test_f(l:list[Animals]):
    for animal in cats_and_dogs:
        if type(animal) is Cat:
            # Здесь - он считает, что это Cat
            animal.Sleep(5)

        elif type(animal) is Dog:
            # Здесь - он считает, что это Dog
            animal.Round()

        # А здесь он считает, что это Animals или его наследники(Cat или Dog)  (т.е. доступны все общие функции)
        animal.Voice()

other_test_f(cats_and_dogs)

for cat in cats:
    cat.Voice()

for dog in dogs:
    dog.Voice()
