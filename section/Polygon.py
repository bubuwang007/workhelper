import numpy as np
import matplotlib.pyplot as plt
from workhelper.section.Section import Section


class Polygon(Section):
    """多边形截面
    points: 多边形顶点坐标(逆时针)
    """

    def __init__(self, points):
        self.points = np.array(points)
        self.x, self.y = [p[0] for p in points], [p[1] for p in points]
        super().__init__((0, 0))

    @property
    def secname(self) -> str:
        return "多边形截面"

    @property
    def symbol(self) -> str:
        return f"多边形"

    @property
    def area(self) -> float:
        x, y = self.x, self.y
        return 0.5 * abs(
            sum(x[i] * y[i + 1] - x[i + 1] * y[i] for i in range(-1, len(x) - 1))
        )

    @property
    def Ix(self) -> float:
        x, y = self.x, self.y
        Ix = (
            sum(
                (y[i] ** 2 + y[i] * y[i + 1] + y[i + 1] ** 2)
                * (x[i] * y[i + 1] - x[i + 1] * y[i])
                for i in range(-1, len(x) - 1)
            )
            / 12
        )
        Ix = Ix - self.area * self.centroid[1] ** 2
        return abs(Ix)

    @property
    def Iy(self) -> float:
        x, y = self.x, self.y
        Iy = (
            sum(
                (x[i] ** 2 + x[i] * x[i + 1] + x[i + 1] ** 2)
                * (x[i] * y[i + 1] - x[i + 1] * y[i])
                for i in range(-1, len(x) - 1)
            )
            / 12
        )
        Iy = Iy - self.area * self.centroid[0] ** 2
        return abs(Iy)

    @property
    def centroid(self):
        x = self.x
        y = self.y
        S = self.area
        xc = sum(
            (x[i] + x[i + 1]) * (x[i] * y[i + 1] - x[i + 1] * y[i])/(6 * S) for i in range(-1, len(x) - 1)
        )
        yc = sum(
            (y[i] + y[i + 1]) * (x[i] * y[i + 1] - x[i + 1] * y[i])/(6 * S) for i in range(-1, len(x) - 1)
        )
        return np.array([xc, yc])

    @centroid.setter
    def centroid(self, value):
        # value = np.array(value)
        # self.points += value - self.centroid
        pass

    @property
    def border(self) -> np.ndarray:
        x, y = self.x, self.y
        return np.array((min(x), max(x), min(y), max(y)))

    def plot(self, show=True):
        plt.gca().set_aspect("equal")
        plt.plot(self.x + [self.x[0]], self.y + [self.y[0]], color="black")
        if show:
            plt.show()


if __name__ == "__main__":
    # points = [(0, 0), (200, 100), (0, 300)]
    # points = [(100, 0), (200, 0), (300, 100),(300, 200),(200, 300), (100, 300), (0, 200), (0, 100)]
    points = [[-240.38590105 ,-175.5       ],
              [  -3.50820229 ,-175.5       ],
              [ 140.5        , -83.42918214],
              [ 140.5        ,  83.42918214],
              [  -3.50820229 , 175.5       ],
              [-240.38590105 , 175.5       ],
              [-335.5        ,  89.66532534],
              [-335.5        , -89.66532534]]
    p = Polygon(points)
    print(p)
    p.plot()
