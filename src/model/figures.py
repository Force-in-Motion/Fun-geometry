

from src.config.output_mess import *
from src.interface.figures import AFigure, AUpgrade




class Star(AFigure):

    def __init__(self, pointer, length, count_angles):
        super().__init__(pointer, length, count_angles)
        self.__count_angles = count_angles
        self.__angle = self.__count_angles // 2 * 360 / self.__count_angles


    def draws(self):
        if  self._rotation_angle % 2 != 0:

            for elem in range(0, self.__count_angles, 1):
                self._pointer.forward(self._length)
                self._pointer.left(self.__angle)

        else:
            print(err_input_star)





class Polygon(AFigure):

    def __init__(self, pointer, length, count_angles):
        super().__init__(pointer, length, 360 / count_angles)
        self.__count_angles = count_angles


    def draws(self):

        for elem in range(0, self.__count_angles, 1):
            self._pointer.forward(self._length)
            self._pointer.left(self._rotation_angle)

















#
# class Triangle:
#     def __init__(self):
#         pass
#
#
#
# class Circle:
#     def __init__(self):
#         pass