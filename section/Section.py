import numpy as np
from abc import ABCMeta, abstractmethod

class Section(metaclass = ABCMeta):
    '''截面基类
    截面图为X-Y平面，X轴为截面的横轴，Y轴为截面的纵轴
    必须要实现的属性：
    area: 截面面积
    secname: 截面名称
    centroid: 截面重心
    Ix: X方向惯性矩
    Iy: Y方向惯性矩
    Ip: 截面极惯性矩
    ix: X方向惯性半径
    iy: Y方向惯性半径
    border: 截面边界，[左边界，右边界，上边界，下边界]
    Wx_left: 左侧X方向截面模量
    Wx_right: 右侧X方向截面模量
    Wy_top: 上侧Y方向截面模量
    Wy_bottom: 下侧Y方向截面模量

    必须要实现的方法：
    plot: 绘制截面
    '''

    def __init__(self, centroid = (0, 0)):
        self.__centroid = np.array(centroid)

    @property
    @abstractmethod
    def area(self) -> float:
        '''面积'''
        pass

    @property
    @abstractmethod
    def secname(self) -> str:
        '''截面名称'''
        pass

    @property
    @abstractmethod
    def symbol(self) -> str:
        '''截面符号与参数'''
        pass

    @property
    def centroid(self) -> np.ndarray:
        '''截面重心'''
        return self.__centroid
    
    @centroid.setter
    def centroid(self, centroid: tuple[float, float]|np.ndarray) -> None:
        self.__centroid = np.array(centroid)

    @abstractmethod
    def plot(self, show=False) -> None:
        '''绘制截面'''
        pass

    @property
    @abstractmethod
    def Ix(self) -> float:
        '''X方向惯性矩'''
        pass

    @property
    @abstractmethod
    def Iy(self) -> float:
        '''Y方向惯性矩'''
        pass

    @property
    def Ip(self) -> float:
        '''截面极惯性矩'''
        return self.Ix + self.Iy

    @property
    def ix(self) -> float:
        '''X方向惯性半径'''
        return np.sqrt(self.Ix / self.area)

    @property
    def iy(self) -> float:
        '''Y方向惯性半径'''
        return np.sqrt(self.Iy / self.area)

    @property
    @abstractmethod
    def border(self) -> np.ndarray:
        '''截面边界 [左边界，右边界，上边界，下边界]'''
        pass

    @property
    def border_left(self) -> float:
        '''左边界'''
        return self.border[0]
    
    @property
    def border_right(self) -> float:
        '''右边界'''
        return self.border[1]
    
    @property
    def border_top(self) -> float:
        '''上边界'''
        return self.border[3]
    
    @property
    def border_bottom(self) -> float:
        '''下边界'''
        return self.border[2]

    @property
    def Wy_left(self) -> float:
        '''左侧X方向截面模量'''
        return self.Iy / abs(self.border_left-self.centroid[0])
    
    @property
    def Wy_right(self) -> float:
        '''右侧X方向截面模量'''
        return self.Iy / abs(self.border_right-self.centroid[0])
    
    @property
    def Wx_top(self) -> float:
        '''上侧Y方向截面模量'''
        return self.Ix / abs(self.border_top-self.centroid[1])
    
    @property
    def Wx_bottom(self) -> float:
        '''下侧Y方向截面模量'''
        return self.Ix / abs(self.border_bottom-self.centroid[1])

    @property
    def Wx(self) -> float:
        '''X方向截面模量'''
        return min(self.Wx_top, self.Wx_bottom)

    @property
    def Wy(self) -> float:
        '''Y方向截面模量'''
        return min(self.Wy_left, self.Wy_right)

    def offset(self, coords: np.ndarray|tuple[float, float]):
        '''坐标偏移'''
        self.centroid += np.array(coords)

    def __str__(self):
        info = [
            f'{self.secname} {self.symbol}',
            f'Area:     {self.area:.9f}',
            f'Ix:       {self.Ix:.9f}',
            f'Iy:       {self.Iy:.9f}',
            f'Ip:       {self.Ip:.9f}',
            f'ix:       {self.ix:.9f}',
            f'iy:       {self.iy:.9f}',
            f'Wx:       {self.Wx:.9f}',
            f'Wy:       {self.Wy:.9f}',
            f'Wx_top:   {self.Wx_top:.9f}',
            f'Wx_bottom:{self.Wx_bottom:.9f}',
            f'Wy_left:  {self.Wy_left:.9f}',
            f'Wy_right: {self.Wy_right:.9f}',
            f'border:   {self.border}',
            f'centroid: {self.centroid}'
        ]
        return '\n'.join(info)