import turtle
from src.model.figures import *
from src.model.upgrade import *
from src.tools.request import RequestUser as ru
from src.config.output_mess import output_msg
class Program:

    def __init__(self):
        self.__turtle = turtle
        self.__pointer = None
        self.__screen_width = None
        self.__screen_height = None






    @staticmethod
    def main():
        print(output_msg.get('greetings'))

        while True:
            ru.get_screen_size()
















if __name__ == "__main__":
    Program.main()