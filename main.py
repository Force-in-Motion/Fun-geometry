import turtle

from src.bl_hight.creator import FigureCreator, ScreenCreator
from src.bl_low.request import RequestUser
from src.config.output_mess import menu_msg
from src.config.config_figures import *


class Program:

    def __init__(self):
        self.__request_user = RequestUser()


    def main(self):
        print(menu_msg.get('greetings'))

        while True:

            screen_creator = ScreenCreator(self.__request_user)

            figure_creator = FigureCreator(config_figures, config_upgrade, self.__request_user)

            pointer = turtle.Turtle()

            window = screen_creator.create_window(turtle)

            figure = figure_creator.create_figure(pointer)

            window.draws()

            figure.draws()

            turtle.mainloop()

            continue_drawing = input(menu_msg.get('continue_drawing')).strip().lower()
            if continue_drawing not in ['да', 'yes', 'y']:
                print(menu_msg.get('Я буду скучать'))
                break




if __name__ == "__main__":
    program = Program()
    program.main()