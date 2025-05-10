import tkinter as tk

import matplotlib.colors as colors
from src.bl_low.response import ResponseUser as ru
from src.config.output_mess import menu_msg, request_data, err_msg
from src.config.config_figures import figure_index




class RequestUser:

    @staticmethod
    def get_max_screen_size():
        root = tk.Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.destroy()

        return width, height


    @staticmethod
    def get_screen_size():
        size = RequestUser.get_max_screen_size()

        print(menu_msg.get('screen_size'))

        while True:
            screen_width = input(f"Введите ширину окна (максимум {size[0]}): ")
            screen_height = input(f"Введите высоту окна (максимум {size[1]}): ")

            if not screen_width.isdigit() or not screen_height.isdigit() or int(screen_width) > size[0] or int(screen_height) > size[1]:
                print(err_msg.get('err_screen_size'))
                continue

            return int(screen_width), int(screen_height)


    @staticmethod
    def get_color_screen():
        list_colors = list(colors.CSS4_COLORS)

        ru.provides_data(list_colors)

        while True:
            color_screen = input(request_data.get('color_screen'))

            if color_screen not in  list_colors:
                print(err_msg.get('err_color'))
                continue

            return color_screen


    @staticmethod
    def get_index_figure():

        while True:
            index = input(menu_msg.get('index_figure'))

            if not index.isdigit() or index not in figure_index:
                print(err_msg.get('err_figure_index'))
                continue

            return index


    @staticmethod
    def get_side_length_figure():
        size = RequestUser.get_max_screen_size()

        while True:
            side_length = input(request_data.get('side_length'))

            if not side_length.isdigit() or  int(side_length) >= size[0] - 100 or int(side_length) >= size[1] - 100:
                print(err_msg.get('err_side_length'))
                continue

            return int(side_length)
        

    @staticmethod
    def get_count_angles_figure():

        while True:
            count_angles = input(request_data.get('count_angles'))

            if not count_angles.isdigit() or  int(count_angles) > 50 :
                print(err_msg.get('err_count_angles'))
                continue

            return int(count_angles)


    @staticmethod
    def get_color_figure():
        list_colors = list(colors.CSS4_COLORS)

        ru.provides_data(list_colors)

        while True:
            color_figure = input(request_data.get('color_figure'))

            if color_figure not in  list_colors:
                print(err_msg.get('err_color'))
                continue

            return color_figure


    @staticmethod
    def get_speed_pointer():

        while True:
            speed_pointer = input(request_data.get('speed_pointer'))

            if not speed_pointer.isdigit() or int(speed_pointer) > 100:
                print(err_msg.get('err_speed_pointer'))
                continue

            return int(speed_pointer)


    @staticmethod
    def get_pen_size():

        while True:
            pen_size = input(request_data.get('pen_size'))

            if not pen_size.isdigit() or int(pen_size) > 100:
                print(err_msg.get('err_pen_size'))
                continue

            return int(pen_size)


    @staticmethod
    def get_action_time():

        while True:
            action_time = input(request_data.get('action_time'))

            if not action_time.isdigit():
                print(err_msg.get('err_action_time'))
                continue

            return int(action_time)
