import numpy as np
import matplotlib.pyplot as plt
from workhelper.section.Section import Section
from itertools import chain


class Combination(Section):
    sections_add: list[Section]
    sections_minus: list[Section]

    def __init__(
        self,
        sections_add: list[Section],
        sections_minus: list[Section] | None = None,
        centroid=(0, 0)
    ):
        if sections_minus is None:
            sections_minus = []
        self.__centroid = np.array(centroid)
        self.sections_add = sections_add
        self.sections_minus = sections_minus
        for sec in chain(self.sections_add, self.sections_minus):
            sec.offset(self.__centroid)

    @property
    def secname(self) -> str:
        return "组合截面"

    @property
    def symbol(self) -> str:
        return "组合截面"

    @property
    def area(self):
        return sum([sec.area for sec in self.sections_add]) - sum(
            [sec.area for sec in self.sections_minus]
        )

    @property
    def Ix(self):
        return sum(
            (
                sec.Ix + sec.area * (sec.centroid[1] - self.centroid[1]) ** 2
                for sec in self.sections_add
            )
        ) - sum(
            (
                sec.Ix + sec.area * (sec.centroid[1] - self.centroid[1]) ** 2
                for sec in self.sections_minus
            )
        )

    @property
    def Iy(self) -> float:
        return sum(
            (
                sec.Iy + sec.area * (sec.centroid[0] - self.centroid[0]) ** 2
                for sec in self.sections_add
            )
        ) - sum(
            (
                sec.Iy + sec.area * (sec.centroid[0] - self.centroid[0]) ** 2
                for sec in self.sections_minus
            )
        )

    @property
    def centroid(self) -> np.ndarray:
        x = (
            sum((sec.centroid[0] * sec.area for sec in self.sections_add))
            - sum((sec.centroid[0] * sec.area for sec in self.sections_minus))
        ) / self.area
        y = (
            sum((sec.centroid[1] * sec.area for sec in self.sections_add))
            - sum((sec.centroid[1] * sec.area for sec in self.sections_minus))
        ) / self.area
        return np.array((x, y))

    @property
    def border(self) -> np.ndarray:
        borders = np.array([sec.border for sec in self.sections_add])
        return np.array(
            (
                borders[:, 0].min(),
                borders[:, 1].max(),
                borders[:, 2].min(),
                borders[:, 3].max(),
            )
        )

    def plot(self, show=True):
        for sec in chain(self.sections_add, self.sections_minus):
            sec.plot(show=False)
        if show:
            plt.show()

    def offset(self, centroid):
        # self.__centroid = np.array(centroid)
        for sec in chain(self.sections_add, self.sections_minus):
            sec.offset(self.__centroid)

    # def __calc_centriod(self, coords):
    #     return np.array(coords)+self.__centroid

if __name__ == "__main__":
    from workhelper.section import Circular, Rectangle, RectanglePipe

    a = Combination(
        [Rectangle(200, 100, (0, 0)), Rectangle(100, 200, (150, 0))],
        # [Rectangle(50,50,(150, 0))]
        [Circular(50, (150, 0))],
        centroid=(100, 100)
    )  # [Rectangle(50,50,(150, 0))]
    print(a)
    a.plot()
