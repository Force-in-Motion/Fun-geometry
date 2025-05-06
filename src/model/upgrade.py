import time

from src.model.figures import *
import turtle


pointer = turtle.Turtle()


class ColorFigure(AUpgrade):

    def __init__(self, pointer, color, wrapper):
        super().__init__(pointer, wrapper)
        self.__color = color


    def draws(self) -> None:
        self._pointer.color(self.__color)
        self._pointer.begin_fill()
        self._wrapper.draws()
        self._pointer.end_fill()



class DrawSpeed(AUpgrade):

    def __init__(self, pointer, speed, wrapper):
        super().__init__(pointer, wrapper)
        self.__speed = speed


    def draws(self) -> None:
        self._pointer.speed(self.__speed)
        self._wrapper.draws()



class PenSize(AUpgrade):

    def __init__(self, pointer, size, wrapper):
        super().__init__(pointer, wrapper)
        self.__size = size


    def draws(self) -> None:
        self._pointer.pensize(self.__size)
        self._wrapper.draws()


class ScreenColor(AUpgrade):

    def __init__(self, turtle, pointer, wrapper, color: str, width: int, height: int):
        super().__init__(pointer, wrapper)
        self._turtle = turtle

        self.__window = turtle.Screen()
        self.__window.bgcolor(color)
        self.__window.setup(width=width, height=height)

    def draws(self) -> None:
        self._wrapper.draws()




s = Star(pointer, 100, 5)
s = ColorFigure(pointer,'green', s)
s = DrawSpeed(pointer, 2, s)
s = PenSize(pointer, 5, s)
s = ScreenColor(turtle, pointer, s,'yellow', 1000, 400, )


s.draws()
time.sleep(3)