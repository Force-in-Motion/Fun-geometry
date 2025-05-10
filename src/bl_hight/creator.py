from src.model.figures import Screen


class FigureCreator:

    def __init__(self, pointer, config_figures, config_upgrade, request_user):
        self.__pointer = pointer
        self.__config_figures = config_figures
        self.__config_upgrade = config_upgrade
        self.__request_user = request_user
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


    def __set_index_figure(self):
        self.__index_figure = self.__request_user.get_index_figure()


    def __set_side_length(self):
        self.__side_length = self.__request_user.get_side_length_figure()


    def __set_count_angles(self):
        self.__count_angles = self.__request_user.get_count_angles_figure()


    def __set_figure_color(self):
        self.__figure_color = self.__request_user.get_color_figure()


    def __set_speed_pointer(self):
        self.__speed_pointer = self.__request_user.get_speed_pointer()


    def __set_pen_size(self):
        self.__pen_size = self.__request_user.get_pen_size()


    def __set_action_time(self):
        self.__action_time = self.__request_user.get_action_time()


    def create_figure(self):
        figure = self.__config_figures.get(self.__index_figure)(self.__pointer, self.__side_length, self.__count_angles)

        figure = self.__config_upgrade.get('color_figure')(self.__pointer, self.__figure_color, figure)

        figure = self.__config_upgrade.get('draw_speed')(self.__pointer, self.__speed_pointer, figure)

        figure = self.__config_upgrade.get('pen_size')(self.__pointer, self.__pen_size, figure)

        figure = self.__config_upgrade.get('timer')(self.__pointer, self.__action_time, figure)

        return figure


class ScreenCreator:

    def __init__(self, turtle, screen, request_user):
        self.__turtle = turtle
        self.__request_user = request_user
        self.__window_width = None
        self.__window_height = None
        self.__window_color = None
        self.__set_window_params()
        self.__set_window_color()

    def __set_window_params(self):
        self.__window_width, self.__window_height = self.__request_user.get_screen_size()


    def __set_window_color(self):
        self.__window_color = self.__request_user.get_color_screen()


    def create_window(self):
        window = Screen(self.__turtle, self.__window_width, self.__window_height, self.__window_color)

        return window
