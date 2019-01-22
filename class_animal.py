# Общий класс для животных
class Animal:
    name = ''
    weight = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print('кормим')

    def voice(self):
        print('голоса')


# Общий класс для птиц
class Bird(Animal):
    def collet_eggs(self):
        print("Собираем яйца")




# Животные
class Cow(Animal):

    def milk(self):
        print('доим')

    def voice(self):
        print('мууууу')


class Sheep(Animal):
    def cut(self):
        print('стрижем')

    def voice(self):
        print('беееее')

class Goat(Cow):
    def voice(self):
        print("Ээээ")


# Птицы
class Chicken(Bird):

    def voice(self):
        print('кукареку')


class Duck(Bird):

    def voice(self):
        print('кря-кря')


class Goose(Bird):
    def voice(self):
        print('га-га')
