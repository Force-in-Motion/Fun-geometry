from src.interface.figures import AFigure



class Star(AFigure):

    def __init__(self, pointer, length, count_angles):
        super().__init__(pointer, length, count_angles)
        self.__count_angles = count_angles
        self.__angle = self.__count_angles // 2 * 360 / self.__count_angles


    def draws(self) -> None:
        for elem in range(0, self.__count_angles, 1):
            self._pointer.forward(self._length)
            self._pointer.left(self.__angle)




class Polygon(AFigure):

    def __init__(self, pointer, length, count_angles):
        super().__init__(pointer, length, 360 / count_angles)
        self.__count_angles = count_angles


    def draws(self):
        for elem in range(0, self.__count_angles, 1):
            self._pointer.forward(self._length)
            self._pointer.left(self._rotation_angle)



















class Circle:
    def __init__(self):
        pass