import turtle

from src.interface.figures import AUpgradeFigure



class ColorFigure(AUpgradeFigure):

    def __init__(self, pointer, figure_color, wrapper):
        super().__init__(pointer, wrapper)
        self.__figure_color = figure_color

    def draws(self) -> None:
        self._pointer.color(self.__figure_color)
        self._pointer.begin_fill()
        self._wrapper.draws()
        self._pointer.end_fill()



class DrawSpeed(AUpgradeFigure):

    def __init__(self, pointer, speed_pointer, wrapper):
        super().__init__(pointer, wrapper)
        self.__speed = speed_pointer

    def draws(self) -> None:
        self._pointer.speed(self.__speed)
        self._wrapper.draws()



class PenSize(AUpgradeFigure):

    def __init__(self, pointer, pen_size, wrapper):
        super().__init__(pointer, wrapper)
        self.__pen_size = pen_size

    def draws(self) -> None:
        self._pointer.pensize(self.__pen_size)
        self._wrapper.draws()



class Timer(AUpgradeFigure):

    def __init__(self, pointer, action_time, wrapper):
        super().__init__(pointer, wrapper)
        self.__action_time = action_time

    def __close_window(self):
        turtle.bye()

    def draws(self) -> None:
        self._wrapper.draws()
        turtle.ontimer(self.__close_window, self.__action_time * 1000)





