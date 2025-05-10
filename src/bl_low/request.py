import tkinter as tk
from curses.ascii import isdigit

import matplotlib.colors as colors
from src.bl_low.response import ResponseUser as ru
from src.config.output_mess import menu_msg
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

            if not isdigit(screen_width) or not isdigit(screen_height) or int(screen_width) > size[0] or int(screen_height) > size[1]:
                print(menu_msg.get('err_screen_size'))
                continue

            return int(screen_width), int(screen_height)


    @staticmethod
    def get_color_screen():
        list_colors = list(colors.CSS4_COLORS)

        ru.provides_data(list_colors)

        while True:
            color_screen = input(menu_msg.get('color_screen'))

            if color_screen not in  list_colors:
                print(menu_msg.get('err_color'))
                continue

            return color_screen


    @staticmethod
    def get_index_figure():

        while True:
            index = input(menu_msg.get('index_figure'))

            if not isdigit(index) or int(index) not in figure_index:
                print(menu_msg.get('err_figure_index'))
                continue

            return int(index)


    @staticmethod
    def get_side_length_figure():
        size = RequestUser.get_max_screen_size()

        while True:
            side_length = input(menu_msg.get('side_length'))

            if not isdigit(side_length) or  int(side_length) >= size[0] - 100 or int(side_length) >= size[1] - 100:
                print(menu_msg.get('err_side_length'))
                continue

            return int(side_length)
        

    @staticmethod
    def get_count_angles_figure():

        while True:
            count_angles = input(menu_msg.get('count_angles'))

            if not isdigit(count_angles) or  int(count_angles) > 50 :
                print(menu_msg.get('err_count_angles'))
                continue

            return count_angles


    @staticmethod
    def get_color_figure():
        list_colors = list(colors.CSS4_COLORS)

        ru.provides_data(list_colors)

        while True:
            color_figure = input(menu_msg.get('color_figure'))

            if color_figure not in  list_colors:
                print(menu_msg.get('err_color'))
                continue

            return color_figure


    @staticmethod
    def get_speed_pointer():

        while True:
            speed_pointer = input(menu_msg.get('speed_pointer'))

            if not isdigit(speed_pointer) or int(speed_pointer) > 100:
                print(menu_msg.get('err_speed_pointer'))
                continue

            return speed_pointer


    @staticmethod
    def get_pen_size():

        while True:
            pen_size = input(menu_msg.get('pen_size'))

            if not isdigit(pen_size) or int(pen_size) > 100:
                print(menu_msg.get('err_pen_size'))
                continue

            return pen_size


    @staticmethod
    def get_action_time():

        while True:
            action_time = input(menu_msg.get('action_time'))

            if not isdigit(action_time) :
                print(menu_msg.get('err_action_time'))
                continue

            return action_time
