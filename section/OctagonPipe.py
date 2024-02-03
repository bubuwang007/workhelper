import numpy as np
from workhelper.section.Combination import Combination
from workhelper.section.Octagon import Octagon
from workhelper.section.Polygon import Polygon
from workhelper.section.utils import clear_float_last_zero as cflz

class OctagonPipe(Combination):
    '''八边形管截面
    v1: X方向长度
    v2: Y方向长度
    v3: 8变形右下角边X方向长度
    v4: 8变形上边X方向长度
    v5: 8变形右边Y方向长度
    v6: 8变形左边Y方向长度
    v7: 壁厚
    '''

    def __init__(self, v1, v2, v3, v4, v5, v6, v7, centroid=(0, 0)):
        self.v1, self.v2, self.v3, self.v4, self.v5, self.v6, self.v7 = v1, v2, v3, v4, v5, v6, v7
        self.__init_sections__()
        self.__check__()
        super().__init__(self.sections_add, self.sections_minus, centroid)
    
    def __check__(self) -> None:
        if self.v1 <= 0 or self.v2 <= 0 or self.v3 <= 0 or self.v4 <= 0 or self.v5 <= 0 or self.v6 <= 0 or self.v7 <= 0:
            raise ValueError("v1,v2,v3,v4,v5,v6,v7 must be positive")
        
    def __init_sections__(self):
        o1 = Octagon(self.v1, self.v2, self.v3, self.v4, self.v5, self.v6)
        self.sections_add = [o1]
        points, innerpoints = o1.points, []
        for i in range(-1, len(points)-1):
            p1, p2, p3 = points[i], points[i - 1], points[i + 1]
            tmp1 = p2[0] - p1[0]
            tmp2 = p2[1] - p1[1]
            tmp3 = p3[0] - p1[0]
            tmp4 = p3[1] - p1[1]
            vec1, vec2 = np.array([tmp1, tmp2]), np.array([tmp3, tmp4])

            vec1len = np.linalg.norm(vec1)
            vec2len = np.linalg.norm(vec2)
            vec1 = vec1 / vec1len
            vec2 = vec2 / vec2len
            vec3 = vec1 + vec2
            vec3len = np.linalg.norm(vec3)
            vec3 = vec3 / vec3len
            cos = np.dot(vec3, vec2)
            sin = np.sqrt(1 - cos**2)
            innerpoints.append((p1[0] + vec3[0] * self.v7 / sin, p1[1] + vec3[1] * self.v7 / sin))
        print(Polygon)
        o2 = Polygon(innerpoints)
        self.sections_minus = [o2]
    
    @property
    def secname(self) -> str:
        return "八边形管截面"
    
    @property
    def symbol(self) -> str:
        v1, v2, v3, v4, v5, v6, v7 = map(cflz, (self.v1, self.v2, self.v3, self.v4, self.v5, self.v6, self.v7))
        return f"O{v1}×{v2}×{v3}×{v4}×{v5}×{v6}×{v7}"

if __name__ == "__main__":
    o = OctagonPipe(500, 375, 152.5, 245, 180, 190, 12)
    print(o)
    o.plot()