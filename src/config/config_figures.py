from src.model.figures import *
from src.model.upgrade import *



figure_index = [1, 2, 3]


figures = {
            '1': Star,
            '2': Circle,
            '3': Polygon
          }


upgrade = {
            'color_figure' : ColorFigure,
            'draw_speed': DrawSpeed,
            'pen_size': PenSize,
            'timer': Timer,
            'screen': Screen
          }