class Figures:
    def __init__(self, name):
        self.name = name
    def perimetr(self):
        pass

class Triangle(Figures):
    def __init__(self, name):
        super().__init__(name)

    def perimetr(self):
        side1 = int(input('Введите первую сторону'))
        side2 = int(input('Введите вторую сторону'))
        side3 = int(input('Введите третью сторону'))
        triangle_perimetr = side1 + side2 + side3
        return triangle_perimetr


class Quadrilateral(Figures):
    def __init__(self, name):
        super().__init__(name)

    def perimetr(self):
        side1 = int(input('Введите первую сторону'))
        side2 = int(input('Введите вторую сторону'))
        side3 = int(input('Введите третью сторону'))
        side4 = int(input('Введите четвертую сторону'))
        quadrilateral_perimetr = side1 + side2 + side3 + side4
        return quadrilateral_perimetr


class Circle(Figures):
    def __init__(self, name):
        super().__init__(name)

    def perimetr(self):
        radius = int(input('Введите радиус'))
        circle_perimetr = radius * 3.14 * 2
        return circle_perimetr

def create_figure():
    figure = input('Переметр какой фигуры надо найти?: (Треугольник, четырехугольник или круг)').strip().lower()

    if figure == 'треугольник':
        return Triangle.perimetr('треугольник')
    elif figure == 'четырехугольник':
        return Quadrilateral.perimetr('четырехугольник')
    elif figure == 'круг':
        return Circle.perimetr('круг')
    else:
        return 'Проверьте написание вашей фигуры'

print(create_figure())

