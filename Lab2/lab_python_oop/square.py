from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, side_param):
        self.side = side_param
        super().__init__(color_param, self.side, self.side)

    def __repr__(self):
        return '{}\nЦвет: {}\nДлинна сторон = {}\nПлощадь = {}'.format(
            Square.get_figure_type(),
            self.color.colorproperty,
            self.side,
            self.square()
        )