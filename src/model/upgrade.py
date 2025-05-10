import turtle
from src.interface.figures import AUpgradeFigure



class ColorFigure(AUpgradeFigure):
    """ Декоратор цвета"""

    def __init__(self, pointer, figure_color, wrapper):
        super().__init__(pointer, wrapper)
        self.__figure_color = figure_color


    def draws(self) -> None:
        """
        добавляет фигуре цвет
        :return: None
        """
        self._pointer.color(self.__figure_color)
        self._pointer.begin_fill()
        self._wrapper.draws()
        self._pointer.end_fill()



class DrawSpeed(AUpgradeFigure):
    """ Декоратор скорость отрисовки"""

    def __init__(self, pointer, speed_pointer, wrapper):
        super().__init__(pointer, wrapper)
        self.__speed = speed_pointer


    def draws(self) -> None:
        """
        Изменяет скорость отрисовки фигуры
        :return: None
        """
        self._pointer.speed(self.__speed)
        self._wrapper.draws()



class PenSize(AUpgradeFigure):
    """ Декоратор толщины пера"""

    def __init__(self, pointer, pen_size, wrapper):
        super().__init__(pointer, wrapper)
        self.__pen_size = pen_size


    def draws(self) -> None:
        """
        Изменяет толщину пера
        :return: None
        """
        self._pointer.pensize(self.__pen_size)
        self._wrapper.draws()



class Timer(AUpgradeFigure):
    """ Декоратор времени действия фигуры"""

    def __init__(self, pointer, action_time, wrapper):
        super().__init__(pointer, wrapper)
        self.__action_time = action_time


    def __close_window(self) -> None:
        """
        Закрывает окно приложения
        :return: None
        """
        turtle.bye()


    def draws(self) -> None:
        """
        Изменяет время действия фигуры
        :return: None
        """
        self._wrapper.draws()
        turtle.ontimer(self.__close_window, self.__action_time * 1000)





