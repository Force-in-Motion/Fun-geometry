import math

from src.interface.figures import AFigure, AScreen



class Star(AFigure):
    """ Геометрическая фигура Звезда """

    def __init__(self, pointer, side_length, count_angles):
        super().__init__(pointer, side_length, count_angles)
        self.__count_angles = count_angles
        self.__angle = self.__count_angles // 2 * 360 / self.__count_angles


    def draws(self) -> None:
        """
        Создает звезду в базовой комплектации
        :return: None
        """
        for elem in range(0, self.__count_angles, 1):
            self._pointer.forward(self._side_length)
            self._pointer.left(self.__angle)





class Polygon(AFigure):
    """ Геометрическая фигура Любой Правильный Многоугольник """

    def __init__(self, pointer, side_length, count_angles):
        super().__init__(pointer, side_length, 360 / count_angles)
        self.__count_angles = count_angles


    def draws(self) -> None:
        """
        Создает Правильный Многоугольник в базовой комплектации
        :return: None
        """
        for elem in range(0, self.__count_angles, 1):
            self._pointer.forward(self._side_length)
            self._pointer.left(self._rotation_angle)





class Circle(AFigure):
    """ Геометрическая фигура Звезда """

    def __init__(self, pointer, side_length, count_angles = None):
        super().__init__(pointer, side_length, count_angles)


    def draws(self) -> None:
        """
        Создает звезду в базовой комплектации
        :return: None
        """
        self._pointer.circle(self._side_length)




class Screen(AScreen):
    """ Холст приложения """

    def __init__(self, turtle, window_width: int, window_height: int, window_color):
        super().__init__(turtle, window_width, window_height)
        self._window_color = window_color


    def draws(self) -> None:
        """
        Создает Холст в базовой комплектации
        :return: None
        """
        self._window = self._turtle.Screen()
        self._window.setup(width=self._window_width, height=self._window_height)
        self._window.bgcolor(self._window_color)