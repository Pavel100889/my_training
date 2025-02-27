class Figure:
    def __init__(self):
        self.__sides = []
        self.__color = []
        self.filled = False

    def __is_valid_color(self, r, g, b):
        return all(isinstance(color, int) and 0 <= color <= 255 for color in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == len(self.__sides) and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__()
        if len(sides) != self.sides_count:
            self.set_sides(1)
        else:
            self.set_sides(*sides)
        self.set_color(*color)

    def get_square(self):
        radius = self.get_sides()[0] / (2 * 3.141592653589793)
        return 3.141592653589793 * (radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__()
        if len(sides) != self.sides_count:
            self.set_sides(1, 1, 1)
        else:
            self.set_sides(*sides)
        self.set_color(*color)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__()
        if len(sides) != self.sides_count:
            self.set_sides(*([1] * self.sides_count))
        else:
            self.set_sides(*([sides[0]] * self.sides_count))
        self.set_color(*color)

    def get_volume(self):
        edge_length = self.get_sides()[0]
        return edge_length ** 3


# Пример использования классов и проверки
if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())  # Ожидается: [55, 66, 77]

    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())  # Ожидается: [222, 35, 130]

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())  # Ожидается: [6, 6,...] (12 раз)

    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())  # Ожидается: [15]

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))  # Ожидается: 15

    # Проверка объёма (куба):
    print(cube1.get_volume())  # Ожидается: 216