
from src.bl_low.request import RequestUser as ru
from src.config.config_figures import *


class FigureCreator:
    """ Сборщик геометрической фигуры в соответствии с параметрами пользователя """

    def __init__(self):
        self.__index_figure = None
        self.__side_length = None
        self.__count_angles = None
        self.__figure_color = None
        self.__speed_pointer = None
        self.__pen_size = None
        self.__action_time = None
        self.__set_index_figure()
        self.__set_side_length()
        self.__set_count_angles()
        self.__set_figure_color()
        self.__set_speed_pointer()
        self.__set_pen_size()
        self.__set_action_time()


    def __set_index_figure(self) -> None:
        """
        Устанавливает индекс, полученный от пользователя
        :return: None
        """
        self.__index_figure = ru.get_index_figure()


    def __set_side_length(self) -> None:
        """
        Устанавливает длину стороны фигуры, полученную от пользователя
        :return: None
        """
        self.__side_length = ru.get_side_length_figure()


    def __set_count_angles(self) -> None:
        """
        Устанавливает количество углов фигуры, полученных от пользователя
        :return: None
        """
        if self.__index_figure != '2':
            self.__count_angles = ru.get_count_angles_figure()

        return


    def __set_figure_color(self) -> None:
        """
        Устанавливает цвет фигуры, полученный от пользователя
        :return: None
        """
        self.__figure_color = ru.get_color_figure()


    def __set_speed_pointer(self) -> None:
        """
        Устанавливает скорость движения поинтера, полученного от пользователя
        :return: None
        """
        self.__speed_pointer = ru.get_speed_pointer()


    def __set_pen_size(self) -> None:
        """
        Устанавливает толщину линии рисования, полученную от пользователя
        :return: None
        """
        self.__pen_size = ru.get_pen_size()


    def __set_action_time(self) -> None:
        """
        Устанавливает время действия рисунка, полученное от пользователя
        :return: None
        """
        self.__action_time = ru.get_action_time()


    def create_figure(self, pointer):
        """
        Собирает воедино фигуру по, заданным пользователем, параметрам, используя паттерн "декоратор"
        :param pointer: pointer
        :return: готовую фигуру
        """
        figure = config_figures.get(self.__index_figure)(pointer, self.__side_length, self.__count_angles)

        figure = config_upgrade.get('color_figure')(pointer, self.__figure_color, figure)

        figure = config_upgrade.get('draw_speed')(pointer, self.__speed_pointer, figure)

        figure = config_upgrade.get('pen_size')(pointer, self.__pen_size, figure)

        figure = config_upgrade.get('timer')(pointer, self.__action_time, figure)

        return figure






class ScreenCreator:
    """ Сборщик холста в соответствии с параметрами пользователя """

    def __init__(self):
        self.__window_width = None
        self.__window_height = None
        self.__window_color = None
        self.__set_window_params()
        self.__set_window_color()

    def __set_window_params(self) -> None:
        """
        Устанавливает параметры окна приложения, полученное от пользователя
        :return: None
        """
        self.__window_width, self.__window_height = ru.get_screen_size()


    def __set_window_color(self) -> None:
        """
        Устанавливает цвет окна приложения, полученное от пользователя
        :return: None
        """
        self.__window_color = ru.get_color_screen()


    def create_window(self, turtle):
        """
        Собирает воедино окно приложения по, заданным пользователем, параметрам
        :param turtle: turtle object
        :return: готовое окно приложения
        """
        window = Screen(turtle, self.__window_width, self.__window_height, self.__window_color)

        return window

