import turtle
from src.bl_hight.creator import FigureCreator, ScreenCreator
from src.config.output_mess import *


class Program:
    """ Ключевой объект приложения """

    @staticmethod
    def main() -> None:
        """
        Запускает главный жизненный цикл приложения
        :return:
        """
        print(menu_msg.get('greetings'))

        while True:

            screen_creator = ScreenCreator()

            figure_creator = FigureCreator()

            pointer = turtle.Turtle()

            window = screen_creator.create_window(turtle)

            figure = figure_creator.create_figure(pointer)

            window.draws()

            figure.draws()

            turtle.mainloop()

            continue_drawing = input(request_data.get('continue_drawing')).strip().lower()

            if continue_drawing not in ['да', 'yes', 'y']:
                print(menu_msg.get('Я буду скучать :( '))
                break


if __name__ == "__main__":
    Program.main()