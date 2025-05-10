from abc import ABC, abstractmethod


class AFigure(ABC):

    def __init__(self, pointer, side_length: int, rotation_angle: float):
        self._pointer = pointer
        self._length = side_length
        self._rotation_angle = rotation_angle


    @abstractmethod
    def draws(self) -> None:
        pass



class AUpgradeFigure(ABC):

    def __init__(self, pointer, wrapper: AFigure):
        self._pointer = pointer
        self._wrapper = wrapper


    def draws(self) -> None:
        pass



class AScreen(ABC):

    def __init__(self, turtle, window_width: int, window_height: int):
        self._turtle = turtle
        self._window_width = window_width
        self._window_height = window_height
        self._window = None

    def draws(self) -> None:
        pass

