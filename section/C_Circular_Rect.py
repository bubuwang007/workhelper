import numpy as np
from workhelper.section.Combination import Combination
try:
    from .Rectangle import Rectangle
    from .CircularPipe import CircularPipe
except ImportError:
    from workhelper.section.Rectangle import Rectangle
    from workhelper.section.CircularPipe import CircularPipe
from workhelper.section.utils import clear_float_last_zero as cflz

class C_Circular_Rect(Combination):
    '''摩擦环截面
    圆管+花纹钢板
    d: 外径
    t: 壁厚
    w: 宽度
    h: 高度
    t1: 腹板厚度
    t2: 竖板厚度
    '''

    def __init__(self, d, t, w, h, t1, t2, centroid=(0, 0)):
        self.d, self.t, self.w, self.h, self.t1, self.t2 = d, t, w, h, t1, t2
        self.__init_sections__()
        super().__init__(self.sections_add, self.sections_minus, centroid)

    def __init_sections__(self):
        r = self.d / 2
        chord = np.sqrt(r**2 - (self.h / 2) ** 2)
        l = self.w + r - chord

        self.sections_add = [
            CircularPipe(self.d, self.t),
            Rectangle(l, self.t1, centroid=(chord + l / 2, self.h / 2 - self.t1 / 2)),
            Rectangle(l, self.t1, centroid=(chord + l / 2, -self.h / 2 + self.t1 / 2)),
            Rectangle(self.t2, self.h - 2 * self.t1, centroid=(r + self.w / 2 - self.t2 / 2, 0)),
            Rectangle(self.t2, self.h - 2 * self.t1, centroid=(r + self.w - 3*self.t2 / 2, 0)),
        ]
        self.sections_minus = []

    @property
    def secname(self) -> str:
        return "摩擦环截面"

    @property
    def symbol(self) -> str:
        d, t, w, h, t1, t2 = map(cflz, (self.d, self.t, self.w, self.h, self.t1, self.t2))
        return f"C{d}×{t}+{w}×{h}×{t1}+{t2}"

if __name__ == "__main__":
    c = C_Circular_Rect(219, 8, 200, 150, 8, 10)
    print(c)
    c.plot()
