class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
            if new_floor > self.number_of_floors or new_floor < 1:
                print("Такого этажа не существует")
            else:
                for i in range (1, new_floor+1):
                    print (i)

h1 = House('Москва', 20)
h2 = House('Владикавказ', 5)
h1.go_to(10)
h2.go_to(8)