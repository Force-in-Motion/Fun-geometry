import turtle
from src.bl_low.request import RequestUser as ru
from src.config.output_mess import menu_msg
from src.model.upgrade import ScreenColor


class Program:

    def __init__(self):
        self.__turtle = turtle
        self.__figure = None
        self.__pointer = self.__turtle.Turtle()
        self.__window_width = None
        self.__window_height = None

    def main(self):
        print(menu_msg.get('greetings'))

        self.__window_width, self.__window_height = ru.get_screen_size()

        screen_color = ScreenColor(self.__turtle, self.__pointer, None, "lightblue", self.__window_width,
                                   self.__window_height)

        # Рисуем цвет фона (это не нарисует ничего само по себе)
        screen_color.draws()

        figure_creator = FigureCreator(self.__pointer, config_figures, config_upgrade)

        # Создаем фигуру на основе ввода пользователя и рисуем ее
        figure = figure_creator.create_figure()

        # Рисуем фигуру в окне графики turtle
        figure.draws()

        # Держим окно открытым до тех пор, пока его не закроет пользователь
        self.__turtle.done()


# Для запуска программы:
if __name__ == "__main__":
    program = Program()
    program.main()