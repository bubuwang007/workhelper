import numpy as np
from workhelper.section.Combination import Combination
from workhelper.section import Rectangle, OctagonPipe
from workhelper.section.utils import clear_float_last_zero as cflz

class C_OctagonPipe_Rect(Combination):
    '''摩擦环截面
    八边形管+花纹钢板
    v1: X方向长度
    v2: Y方向长度
    v3: 8变形右下角边X方向长度
    v4: 8变形上边X方向长度
    v5: 8变形右边Y方向长度
    v6: 8变形左边Y方向长度
    v7: 壁厚
    v8: 宽度
    v9: 高度
    v10: 腹板厚度
    v11: 竖板厚度
    '''

    def __init__(self, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, centroid=(0, 0)):
        self.v1, self.v2, self.v3, self.v4, self.v5, self.v6, self.v7, self.w, self.h, self.t1, self.t2 = v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11
        self.__init_sections__()
        super().__init__(self.sections_add, self.sections_minus, centroid)

    def __init_sections__(self):
        o = OctagonPipe(self.v1, self.v2, self.v3, self.v4, self.v5, self.v6, self.v7)
        self.sections_add = [o,
            Rectangle(self.w, self.t1, centroid=(self.v3+self.w / 2, self.h / 2 - self.t1 / 2)),
            Rectangle(self.w, self.t1, centroid=(self.v3+self.w / 2, -self.h / 2 + self.t1 / 2)),
            Rectangle(self.t2, self.h - 2 * self.t1, centroid=(self.v3 + self.w / 2 - self.t2 / 2, 0)),
            Rectangle(self.t2, self.h - 2 * self.t1, centroid=(self.v3 + self.w - 3*self.t2 / 2, 0))
        ]
        self.sections_minus = []

    @property
    def secname(self) -> str:
        return "摩擦环截面"
    
    @property
    def symbol(self) -> str:
        v1, v2, v3, v4, v5, v6, v7, w, h, t1, t2 = map(cflz, (self.v1, self.v2, self.v3, self.v4, self.v5, self.v6, self.v7, self.w, self.h, self.t1, self.t2))
        return f"O{v1}×{v2}×{v3}×{v4}×{v5}×{v6}×{v7}+{w}×{h}×{t1}+{t2}"

if __name__ == "__main__":
    c = C_OctagonPipe_Rect(500, 375, 152.5, 245, 180, 190, 12, 250, 150, 6, 6)
    print(c)
    c.plot()