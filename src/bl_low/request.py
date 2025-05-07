import tkinter as tk
from curses.ascii import isdigit

import matplotlib.colors as colors
from src.bl_low.response import ResponseUser as ru
from src.config.output_mess import menu_msg
from src.config.figures import figure_index




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
                print(menu_msg.get('err_color_figure'))
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




#
#
# # Определяем размеры фигур
# def get_figure_size(figure_type, size):
#     if figure_type == "star":
#         return size * 2  # Примерный размер звезды
#     elif figure_type == "circle":
#         return size * 2  # Диаметр круга
#     elif figure_type == "rectangle":
#         return size * 2, size  # Ширина и высота прямоугольника
#     # Добавьте другие фигуры по мере необходимости
#     return size
#
#
# # Универсальный метод для проверки размещения фигур в окне
# def can_fit_in_window(window_width, window_height, figures):
#     total_width = 0
#     max_height = 0
#
#     for figure in figures:
#         figure_type = figure['type']
#         size = figure['size']
#
#         if figure_type in ["star", "circle"]:
#             width = get_figure_size(figure_type, size)
#             height = width  # Для звезды и круга ширина равна высоте
#         elif figure_type == "rectangle":
#             width, height = get_figure_size(figure_type, size)
#
#         total_width += width
#
#         if height > max_height:
#             max_height = height
#
#     # Проверяем помещается ли общая ширина и максимальная высота в окно
#     return total_width <= window_width and max_height <= window_height
#
#
# # Пример использования
# window_width = 800
# window_height = 600
#
# # Список фигур с их типами и размерами
# figures = [
#     {'type': 'star', 'size': 20},
#     {'type': 'circle', 'size': 30},
#     {'type': 'rectangle', 'size': 40}  # Прямоугольник с размером стороны 40 (ширина и высота)
# ]
#
# if can_fit_in_window(window_width, window_height, figures):
#     print("Все фигуры помещаются в окно.")
# else:
#     print("Фигуры не помещаются в окно.")
#

