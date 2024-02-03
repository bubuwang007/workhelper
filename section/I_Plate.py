from workhelper.section.Combination import Combination
from workhelper.section import Rectangle, I
from workhelper.section.utils import clear_float_last_zero as cflz

class I_Plate(Combination):
    '''工字钢+竖板
    h: 高度(y轴方向)
    w: 宽度(x轴方向)
    tw: 腹板厚度
    tf: 翼缘厚度
    t: 竖板厚度
    '''

    def __init__(self, h, w, tw, tf, t, centroid=(0, 0)):
        self.h, self.w, self.tw, self.tf, self.t = h, w, tw, tf, t
        self.__init_sections__()
        super().__init__(self.sections_add, self.sections_minus, centroid)
    
    def __init_sections__(self):
        self.sections_add = [
            I(self.h, self.w, self.tw, self.tf),
            Rectangle(self.t, self.h-2*self.tf, centroid=(self.w/2-3*self.t/2, 0)),
        ]
        self.sections_minus = []
    
    @property
    def secname(self) -> str:
        return "工字钢+竖板"

    @property
    def symbol(self) -> str:
        h, w, tw, tf, t = map(cflz, (self.h, self.w, self.tw, self.tf, self.t))
        return f"I{h}×{w}×{tw}×{tf}×{t}"

if __name__ == "__main__":
    i = I_Plate(200, 200, 8, 12, 10)
    print(i)
    i.plot()