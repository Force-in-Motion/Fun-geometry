import tkinter as tk

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
            screen_width = int(input(f"Введите ширину окна (максимум {size[0]}): "))
            screen_height = int(input(f"Введите высоту окна (максимум {size[1]}): "))

            if screen_width > size[0] or screen_height > size[1]:
                print(menu_msg.get('err_screen_size'))
                continue

            return screen_width, screen_height


    @staticmethod
    def get_index_figure():

        while True:
            index = int(input(menu_msg.get('index_figure')))
            if index not in figure_index:
                print(menu_msg.get('err_figure_index'))
                continue

            return index


    @staticmethod
    def get_side_length_figure():
        size = RequestUser.get_max_screen_size()

        while True:
            length = int(input(menu_msg.get('length')))
            if length >= size[0] - 100 or length >= size[1] - 100:
                print(menu_msg.get('err_length'))
                continue

            return length
        

    @staticmethod
    def get_count_angles_figure():

        while True:
            count_angles = int(input(menu_msg.get('count_angles')))
            if count_angles > 50:
                print(menu_msg.get('err_count_angles'))
                continue

            return count_angles

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

