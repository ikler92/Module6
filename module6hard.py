import math


class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.__color = list(color)
        self.filled = False

        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            if self.__is_valid_sides(*sides):
                self.__sides = list(sides)
            else:
                self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        if isinstance(r, int) and 0 <= r <= 255:
            if isinstance(g, int) and 0 <= g <= 255:
                if isinstance(b, int) and 0 <= b <= 255:
                    return True
        return False

    def set_color(self, r, g, b):
        if Figure.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        a, b, c = self.get_sides()
        s = sum(self.get_sides()) / 2  # Полупериметр
        return (2 / a) * math.sqrt(s * (s - a) * (s - b) * (s - c))

    def get_square(self):
        a = self.get_sides()[0]
        return 0.5 * a * self.__height


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.set_sides(sides[0])
        else:
            self.set_sides(1)

    def set_sides(self, *sides):
        if len(sides) == 1 and isinstance(sides[0], int) and sides[0] > 0:
            self._Figure__sides = [sides[0]] * self.sides_count

    def get_volume(self):
        return self.get_sides()[0] ** 3


# Проверка кода

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
