import numpy as np
from workhelper.section.Combination import Combination
try:
    from .RectanglePipe import RectanglePipe
    from .CircularPipe import CircularPipe
except ImportError:
    from workhelper.section.RectanglePipe import RectanglePipe
    from workhelper.section.CircularPipe import CircularPipe
from workhelper.section.utils import clear_float_last_zero as cflz

class C_Circular_Rect0(Combination):
    '''摩擦环截面
    圆管+花纹钢板
    d: 外径
    t: 壁厚
    w: 矩形管宽度
    h: 矩形管高度
    t1: 腹板厚度
    '''

    def __init__(self, d, t, w, h, t1, centroid=(0, 0)):
        self.d, self.t, self.w, self.h, self.t1 = d, t, w, h, t1
        self.__init_sections__()
        super().__init__(self.sections_add, self.sections_minus, centroid)

    def __init_sections__(self):
        r = self.d / 2
        self.sections_add = [
            CircularPipe(self.d, self.t),
            RectanglePipe(self.w, self.h, self.t1, self.t1, centroid=(r+self.w/2, 0)),
        ]
        self.sections_minus = []

    @property
    def secname(self) -> str:
        return "摩擦环截面"

    @property
    def symbol(self) -> str:
        d, t, w, h, t1 = map(cflz, (self.d, self.t, self.w, self.h, self.t1))
        return f"C{d}×{t}+{w}×{h}×{t1}"

if __name__ == "__main__":
    c = C_Circular_Rect0(219, 8, 200, 150, 8)
    print(c)
    c.plot()
