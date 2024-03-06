import numpy as np
import matplotlib.pyplot as plt
from workhelper.section.Section import Section
from workhelper.section.utils import clear_float_last_zero as cflz

class InclineRectangle(Section):
    '''斜矩形截面
    w: 宽度(x轴方向)
    h: 高度(y轴方向)
    theta: 倾斜角度(与x轴正方向的夹角)
    '''

    def __init__(self, w, h, theta, centroid=(0, 0)):
        super().__init__(centroid)
        self.w, self.h, self.theta = w, h, theta/180*np.pi
        self.__check__()

    def __check__(self) -> None:
        if self.w <= 0 or self.h <= 0:
            raise ValueError("w and h must be positive")
    
    @property
    def secname(self) -> str:
        return "斜矩形截面"
    
    @property
    def symbol(self) -> str:
        w, h, theta = map(cflz, (self.w, self.h, self.theta))
        return f"{w}×{h}×{theta}°"
    
    @property
    def area(self)->float:
        return self.w * self.h
    
    @property
    def Ix(self) -> float:
        return self.w * self.h**3 / 12*np.cos(self.theta)**2 + self.w**3 * self.h / 12*np.sin(self.theta)**2
    
    @property
    def Iy(self) -> float:
        return self.w * self.h**3 / 12*np.sin(self.theta)**2 + self.w**3 * self.h / 12*np.cos(self.theta)**2
    
    @property
    def border(self) -> np.ndarray:
        # 旋转了theta角度
        theta = self.theta
        return np.array((
            -self.w / 2 * np.cos(theta) - self.h / 2 * np.sin(theta) + self.centroid[0],
            self.w / 2 * np.cos(theta) + self.h / 2 * np.sin(theta) + self.centroid[0],
            -self.w / 2 * np.sin(theta) - self.h / 2 * np.cos(theta) + self.centroid[1],
            self.w / 2 * np.sin(theta) + self.h / 2 * np.cos(theta) + self.centroid[1]
        ))
    
    def plot(self, show=True):
        plt.gca().set_aspect("equal")
        # 画矩形
        theta = self.theta
        x = (
            np.array((-self.w / 2, self.w / 2, self.w / 2, -self.w / 2, -self.w / 2))
            * np.cos(theta)
            - np.array((-self.h / 2, -self.h / 2, self.h / 2, self.h / 2, -self.h / 2))
            * np.sin(theta)
            + self.centroid[0]
        )
        y = (
            np.array((-self.w / 2, self.w / 2, self.w / 2, -self.w / 2, -self.w / 2))
            * np.sin(theta)
            + np.array((-self.h / 2, -self.h / 2, self.h / 2, self.h / 2, -self.h / 2))
            * np.cos(theta)
            + self.centroid[1]
        )
        plt.plot(x, y, color="black")
        if show:
            plt.show()
    
if __name__ == "__main__":
    r = InclineRectangle(200, 100, 30, (100, 200))
    print(r)
    r.plot()