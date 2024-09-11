class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
            if new_floor > self.number_of_floors or new_floor < 1:
                print("Такого этажа не существует")


h1 = House('Москва', 20)
h1.go_to(30)
