import numpy as np
import matplotlib.pyplot as plt
from workhelper.section.Section import Section
from workhelper.section.utils import clear_float_last_zero as cflz

class RectanglePipe(Section):
    '''矩形管截面
    w: 宽度(x轴方向)
    h: 高度(y轴方向)
    tw: 壁厚(x轴方向)
    th: 腹板厚度(y轴方向)
    '''

    def __init__(self, w, h, tw, th, centroid=(0, 0)):
        super().__init__(centroid)
        self.w, self.h, self.tw, self.th = w, h, tw, th
        self.__check__()

    def __check__(self) -> None:
        if self.w <= 0 or self.h <= 0:
            raise ValueError("w and h must be positive")
        if self.tw >= self.w / 2 or self.th >= self.h / 2:
            raise ValueError("t1 and t2 must be smaller than w/2 and h/2")

    @property
    def secname(self) -> str:
        return "矩形管截面"
    
    @property
    def symbol(self) -> str:
        w, h, tw, th = map(cflz, (self.w, self.h, self.tw, self.th))
        return f"{w}×{h}×{tw}×{th}"

    @property
    def area(self):
        return self.w * self.h - (self.w - 2 * self.tw) * (self.h - 2 * self.th)
    
    @property
    def Ix(self) -> float:
        return (
            self.w * self.h**3 / 12
            - (self.w - 2 * self.tw) * (self.h - 2 * self.th) ** 3 / 12
        )
    
    @property
    def Iy(self) -> float:
        return (
            self.w**3 * self.h / 12
            - (self.w - 2 * self.tw) ** 3 * (self.h - 2 * self.th) / 12
        )
    
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
        # 画内矩形
        x1 = (
            np.array(
                (
                    -self.w / 2 + self.tw,
                    self.w / 2 - self.tw,
                    self.w / 2 - self.tw,
                    -self.w / 2 + self.tw,
                    -self.w / 2 + self.tw,
                )
            )
            + self.centroid[0]
        )
        y1 = (
            np.array(
                (
                    -self.h / 2 + self.th,
                    -self.h / 2 + self.th,
                    self.h / 2 - self.th,
                    self.h / 2 - self.th,
                    -self.h / 2 + self.th,
                )
            )
            + self.centroid[1]
        )
        plt.plot(x1, y1, color="black")
        if show:
            plt.show()

if __name__ == "__main__":
    r = RectanglePipe(200, 100, 20, 10)
    print(r)
    r.plot()