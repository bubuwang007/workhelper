import numpy as np
import matplotlib.pyplot as plt
from workhelper.section.Section import Section
from workhelper.section.utils import clear_float_last_zero as cflz

class Rectangle(Section):
    '''矩形截面
    w: 宽度(x轴方向)
    h: 高度(y轴方向)
    '''

    def __init__(self, w, h, centroid=(0, 0)):
        super().__init__(centroid)
        self.w, self.h = w, h
        self.__check__()

    def __check__(self) -> None:
        if self.w <= 0 or self.h <= 0:
            raise ValueError("w and h must be positive")

    @property
    def secname(self) -> str:
        return "矩形截面"

    @property
    def symbol(self) -> str:
        w, h = map(cflz, (self.w, self.h))
        return f"{w}×{h}"

    @property
    def area(self)->float:
        return self.w * self.h

    @property
    def Ix(self) -> float:
        return self.w * self.h**3 / 12

    @property
    def Iy(self) -> float:
        return self.w**3 * self.h / 12

    @property
    def border(self) -> np.ndarray:
        return np.array((-self.w / 2+ self.centroid[0], self.w / 2+ self.centroid[0],
                         -self.h / 2+ self.centroid[1], self.h / 2+ self.centroid[1]))

    def plot(self, show=True):
        plt.gca().set_aspect("equal")
        # 画矩形
        x = (
            np.array((-self.w / 2, self.w / 2, self.w / 2, -self.w / 2, -self.w / 2))
            + self.centroid[0]
        )
        y = (
            np.array((-self.h / 2, -self.h / 2, self.h / 2, self.h / 2, -self.h / 2))
            + self.centroid[1]
        )
        plt.plot(x, y, color="black")
        if show:
            plt.show()

if __name__ == "__main__":
    r = Rectangle(200, 100)
    print(r)
    r.plot()