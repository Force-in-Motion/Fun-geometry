from abc import ABC, abstractmethod


class AFigure(ABC):

    def __init__(self, pointer, length: int, rotation_angle: float):
        self._pointer = pointer
        self._length = length
        self._rotation_angle = rotation_angle


    @abstractmethod
    def draws(self) -> None:
        pass




class AUpgrade(ABC):

    def __init__(self, pointer, wrapper: AFigure):
        self._pointer = pointer
        self._wrapper = wrapper


    def draws(self) -> None:
        pass


