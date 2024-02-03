from workhelper.section.Combination import Combination
from workhelper.section import Rectangle
from workhelper.section.utils import clear_float_last_zero as cflz

class I(Combination):
    '''工字钢
    h: 高度(y轴方向)
    w: 宽度(x轴方向)
    tw: 腹板厚度
    tf: 翼缘厚度
    '''

    def __init__(self, h, w, tw, tf, centroid=(0, 0)):
        self.h, self.w, self.tw, self.tf = h, w, tw, tf
        self.__check__()
        self.__init_sections__()
        super().__init__(self.sections_add, self.sections_minus, centroid)

    def __check__(self) -> None:
        if self.h <= 0 or self.w <= 0 or self.tw <= 0 or self.tf <= 0:
            raise ValueError("h, w, tw and tf must be positive")
        if self.tf >= self.h / 2 or self.tw >= self.w / 2:
            raise ValueError("tf and tw must be smaller than h/2 and w/2")

    def __init_sections__(self):
        self.sections_add = [
            Rectangle(self.tw, self.h-2*self.tf),
            Rectangle(self.w, self.tf, centroid=(0, (self.h-self.tf)/2)),
            Rectangle(self.w, self.tf, centroid=(0, -(self.h-self.tf)/2)),
        ]
        self.sections_minus = []

    @property
    def secname(self) -> str:
        return "工字钢"

    @property
    def symbol(self) -> str:
        h, w, tw, tf = map(cflz, (self.h, self.w, self.tw, self.tf))
        return f"I{h}×{w}×{tw}×{tf}"

if __name__ == "__main__":
    i = I(200, 200, 8, 12)
    print(i)
    i.plot()