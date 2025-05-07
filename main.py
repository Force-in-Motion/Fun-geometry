import turtle
from src.bl_low.request import RequestUser as ru
from src.config.output_mess import menu_msg
from src.config.figures import figure




class Program:

    def __init__(self):
        self.__turtle = turtle
        self.__figure = None
        self.__pointer = None
        self.__window_width = None
        self.__window_height = None


    def main(self):
        print(menu_msg.get('greetings'))

        while True:
            self.__window_width, self.__window_height = ru.get_screen_size()

            index = ru.get_index_figure()

            self.__figure = figure.get(index)()
















if __name__ == "__main__":
    p = Program()
    p.main()