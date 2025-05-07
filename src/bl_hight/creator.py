
class FigureCreator:

    def __init__(self, request_user, index):
        self.__request_user = request_user
        self.__index_figure = index
        self.__side_length = None
        self.__count_angles = None
        self.__figure_color = None
        self.__speed_pointer = None
        self.__pen_size = None
        self.__action_time = None

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