import math
from workhelper.section.Combination import Combination

try:
    from CircularPipe import CircularPipe
    from InclineRectangle import InclineRectangle
except ImportError:
    from .CircularPipe import CircularPipe
    from .InclineRectangle import InclineRectangle
from workhelper.section.utils import clear_float_last_zero as cflz

class P_MultiCircularPipe(Combination):
    '''多根圆管组合的主轴截面
    d1: 中心圆管直径
    t1: 中心圆管壁厚
    r12: 中心圆管圆心到外圆管圆心的距离
    num: 外圆管数量
    d2: 外圆管直径
    t2: 外圆管壁厚
    '''

    def __init__(self, d1, t1, r12, num, d2, t2, centroid=(0, 0)):
        self.d1, self.t1, self.r12, self.num, self.d2, self.t2 = d1, t1, r12, num, d2, t2
        self.__init_sections__()
        super().__init__(self.sections_add, self.sections_minus, centroid)

    
    def __init_sections__(self):
        self.sections_add = [
            CircularPipe(self.d1, self.t1, centroid=(0, 0)),
        ]

        inter_angle = 2 * math.pi / self.num
        w = 0.001
        h = self.r12 - self.d1/2 - self.d2/2 + self.t1/2 + self.t2/2
        for i in range(self.num):
            ang = i * inter_angle
            ang_deg = ang / math.pi * 180

            x = self.r12 * math.sin(ang)
            y = self.r12 * math.cos(ang)
            cp = CircularPipe(self.d2, self.t2, centroid=(x, y))
            self.sections_add.append(cp)

            x1 = (self.d1/2 - self.t1/2 + h/2) * math.sin(ang)
            y1 = (self.d1/2 - self.t1/2 + h/2) * math.cos(ang)

            self.sections_add.append(InclineRectangle(w, h, -ang_deg, centroid=(x1, y1)))

        self.sections_minus = []

    @property
    def secname(self) -> str:
        return "多根圆管组合的主轴截面"
    
    @property
    def symbol(self) -> str:
        d1, t1, r12, num, d2, t2 = map(cflz, (self.d1, self.t1, self.r12, self.num, self.d2, self.t2))
        return f"Φ({d1}×{t1})+({r12}+Φ{d2}×{t2})×{num}"
    
if __name__ == "__main__":
    p = P_MultiCircularPipe(0.630, 0.02, 0.6, 6, 0.14, 0.01)
    print(p)
    p.plot()