from workhelper.section.Combination import Combination
from .Rectangle import Rectangle
from workhelper.section.utils import clear_float_last_zero as cflz

class L(Combination):
    '''角钢'''

    def __init__(self, l, t, centroid=(0, 0)):
        self.l, self.t = l, t
        self.__check__()
        self.__init_sections__()
        super().__init__(self.sections_add, self.sections_minus, centroid)

    def __check__(self) -> None:
        if self.l <= 0 or self.t <= 0:
            raise ValueError("l and t must be positive")

    def __init_sections__(self):
        self.sections_add = [
            Rectangle(self.l-self.t, self.t, centroid=(self.l/2+self.t/2, self.t/2)),
            Rectangle(self.t, self.l, centroid=(self.t/2, self.l/2)),
        ]
        self.sections_minus = []

    @property
    def secname(self) -> str:
        return "角钢"

    @property
    def symbol(self) -> str:
        l, t = map(cflz, (self.l, self.t))
        return f"L{l}×{t}"

if __name__ == "__main__":
    i = L(200, 20, centroid=(10,10))
    print(i)
    i.plot()