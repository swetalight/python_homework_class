from class_animal import *

goose_grey = Goose("Серый", 5)
goose_white = Goose("Белый", 10)
cow = Cow("Манька", 120)
sheep = Sheep("Барашек", 55)
sheep_2 = Sheep("Кудрявый", 60)
chicken = Chicken("Ко-ко", 4)
chicken2 = Chicken("Кукареку", 3)
goat = Goat("Рога", 30)
goat2 = Goat("Копыта", 45)
duck = Duck("Кряква", 15)

goose_grey.feed()
goose_white.feed()
cow.feed()
sheep.feed()
sheep_2.feed()
chicken.feed()
chicken2.feed()
goat.feed()
goat2.feed()
duck.feed()
cow.milk()
goat.milk()
goat2.milk()
sheep.cut()
sheep_2.cut()
goose_grey.collet_eggs()
goose_white.collet_eggs()
chicken.collet_eggs()
chicken2.collet_eggs()

all_weight = goose_grey.weight + goose_white.weight + cow.weight + sheep.weight + sheep_2.weight + chicken.weight + chicken2.weight + goat.weight + goat2.weight + duck.weight
print('Общий вес животных на ферме :', all_weight)
list_weight: Animal = [goose_grey, goose_white, cow, sheep, sheep_2, chicken, chicken2, goat, goat2, duck]


def custom_max(array):
    max = 0
    name = ""
    for i in array:
        if i.weight > max:
            max = i.weight
            name = i.name
    return name


big_weight = custom_max(list_weight)
print("Самое тяжелое животное: " + big_weight)
