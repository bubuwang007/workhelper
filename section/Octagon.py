from workhelper.section.Polygon import Polygon
from workhelper.section.utils import clear_float_last_zero as cflz

class Octagon(Polygon):
    '''八边形截面
    v1: X方向长度
    v2: Y方向长度
    v3: 8变形右下角边X方向长度
    v4: 8变形上边X方向长度
    v5: 8变形右边Y方向长度
    v6: 8变形左边Y方向长度
    '''
    def __init__(self, v1, v2, v3, v4, v5, v6, centroid=(0, 0)):
        self.v1, self.v2, self.v3, self.v4, self.v5, self.v6= v1, v2, v3, v4, v5, v6
        self.__init_sections__()
        self.__check__()
        super().__init__(self.points)

    def __check__(self) -> None:
        if self.v1 <= 0 or self.v2 <= 0 or self.v3 <= 0 or self.v4 <= 0 or self.v5 <= 0 or self.v6 <= 0:
            raise ValueError("v1,v2,v3,v4,v5,v6,v7 must be positive")

    def __init_sections__(self):
        x1 = self.v3-self.v1
        x2 = -self.v4
        x3 = 0
        x4 = self.v3
        y1 = -self.v2 / 2
        y2 = -self.v6 / 2
        y3 = self.v6 / 2
        y4 = self.v2 / 2
        y5 = -self.v5 / 2
        y6 = self.v5 / 2

        self.points = [
            (x3, y1),
            (x4, y5),
            (x4, y6),
            (x3, y4),
            (x2, y4),
            (x1, y3),
            (x1, y2),
            (x2, y1),
        ]

    @property
    def secname(self) -> str:
        return "八边形截面"

    @property
    def symbol(self) -> str:
        v1, v2, v3, v4, v5, v6 = map(cflz, (self.v1, self.v2, self.v3, self.v4, self.v5, self.v6))
        return f"{v1}×{v2}×{v3}×{v4}×{v5}×{v6}"
    
if __name__ == "__main__":
    o = Octagon(500, 375, 152.5, 245, 180, 190)
    print(o)
    o.plot()

