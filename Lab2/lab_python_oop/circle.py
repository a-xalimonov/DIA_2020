from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math

class Circle(Figure):
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, radius_param):
        self.radius = radius_param
        self.color = FigureColor()
        self.color.colorproperty = color_param

    def square(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return '{}\nЦвет: {}\nРадиус = {}\nПлощадь = {}'.format(
            Circle.get_figure_type(),
            self.color.colorproperty,
            self.radius,
            self.square()
        )