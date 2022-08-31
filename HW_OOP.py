#Hometask_14_1 Hometask_14_2
class Dog:
    """
    Выполняет работу с объектами
    """

    def __init__(self,height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self,l):
        print(f'Собака с именем {self.name} прыгает на {l} метров')

    def run(self,speed,distance):
        print(f'Собака породы {self.name} бегает на дистанции {distance} метров со скоростью {speed} километров в час')

    def bark(self,f):
        if f == "Yes":
            print(f'Собака {self.name} лает')
        else:
            print(f'Собака {self.name} не лает')

    def change_name(self):
        new_name = input("Введите новое имя собаки:")
        self.name = new_name

metis = Dog(40,80,"Astra",1)
sheepdog = Dog(80,120,"Zuk",4)

print(metis.__dict__)
print(sheepdog.__dict__)
print(metis.jump(1.5))
print(sheepdog.run(30,4000))
print(sheepdog.bark("Yes"))
print(metis.name)
Dog.change_name(metis)
print(metis.name)
